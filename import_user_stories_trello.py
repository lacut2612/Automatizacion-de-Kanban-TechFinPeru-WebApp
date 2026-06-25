import csv
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


API_BASE = "https://api.trello.com/1"
CSV_PATH = Path("user_stories.csv")
ENV_PATH = Path(".env")
BOARD_NAME = "Coolbox B2B WebApp"
COLUMNS = ["Product Backlog", "To Do", "In Progress", "Testing", "Done"]
INITIAL_LIST = "Product Backlog"
LABEL_COLORS = ["green", "yellow", "orange", "red", "purple", "blue", "sky", "lime", "pink", "black"]
DEFAULT_WIP_LIMITS = {
    "To Do": 5,
    "In Progress": 3,
    "Testing": 3,
}


def load_env():
    if not ENV_PATH.exists():
        return

    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def credentials():
    load_env()
    api_key = os.getenv("TRELLO_API_KEY", "").strip()
    token = os.getenv("TRELLO_TOKEN", "").strip()

    if not api_key or not token:
        raise SystemExit(
            "Faltan TRELLO_API_KEY y/o TRELLO_TOKEN en .env.\n"
            "Genera un token con esta URL, reemplazando YOUR_KEY:\n"
            "https://trello.com/1/authorize?expiration=never&name=CoolboxB2BImporter&scope=read,write&response_type=token&key=YOUR_KEY"
        )

    return api_key, token


def trello(method, path, params=None, check=True):
    api_key, token = credentials()
    query = {
        **(params or {}),
        "key": api_key,
        "token": token,
    }
    url = f"{API_BASE}{path}?{urllib.parse.urlencode(query, doseq=True)}"
    request = urllib.request.Request(url, method=method)

    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8")
        message = f"{method} {path}: {detail}"

        if not check:
            print(f"Advertencia: {message}", file=sys.stderr)
            return None

        print(message, file=sys.stderr)
        raise SystemExit(error.code)


def read_rows():
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def labels_from(row):
    raw_labels = row.get("Etiquetas (labels)", "")
    return [
        label.strip()
        for label in raw_labels.replace(";", ",").split(",")
        if label.strip()
    ]


def card_description(row):
    sections = []

    for column, value in row.items():
        value = (value or "").strip()
        if column in ["Titulo", "Etiquetas (labels)"] or not value:
            continue
        sections.append(f"## {column}\n\n{value}")

    sections.append(f"_Importado desde `{CSV_PATH.name}`._")
    return "\n\n".join(sections)


def delete_existing_boards():
    boards = trello("GET", "/members/me/boards", {"fields": "name,url,closed"})

    for board in boards:
        if board["name"] != BOARD_NAME:
            continue

        print(f"Borrando tablero existente: {board['name']} ({board.get('url', board['id'])})")
        trello("DELETE", f"/boards/{board['id']}")


def create_board():
    print(f"Creando tablero Trello: {BOARD_NAME}")
    return trello("POST", "/boards/", {
        "name": BOARD_NAME,
        "defaultLists": "false",
        "prefs_permissionLevel": "private",
    })


def list_display_name(name):
    if name in DEFAULT_WIP_LIMITS:
        return f"{name} (WIP {DEFAULT_WIP_LIMITS[name]})"

    return name


def set_wip_limit(list_id, limit):
    result = trello("PUT", f"/lists/{list_id}/softLimit", {
        "value": limit,
    }, check=False)
    return result is not None


def cards_in_list(list_id):
    return trello("GET", f"/lists/{list_id}/cards", {
        "fields": "id",
    })


def enforce_wip_limit(list_name, list_id):
    if list_name not in DEFAULT_WIP_LIMITS:
        return

    current_count = len(cards_in_list(list_id))
    limit = DEFAULT_WIP_LIMITS[list_name]

    if current_count >= limit:
        raise SystemExit(
            f"WIP limit alcanzado en '{list_name}': "
            f"{current_count}/{limit}. No se creo la tarjeta."
        )


def validate_wip_limits(lists):
    summaries = []

    for list_name, limit in DEFAULT_WIP_LIMITS.items():
        count = len(cards_in_list(lists[list_name]))

        if count > limit:
            raise SystemExit(f"WIP limit excedido en '{list_name}': {count}/{limit}.")

        summaries.append(f"{list_name} {count}/{limit}")

    print(f"WIP limits validados: {', '.join(summaries)}.")


def create_lists(board_id):
    lists = {}

    for index, name in enumerate(COLUMNS, start=1):
        params = {
            "name": list_display_name(name),
            "idBoard": board_id,
            "pos": index,
        }

        print(f"Creando lista: {params['name']}")
        trello_list = trello("POST", "/lists", params)

        if name in DEFAULT_WIP_LIMITS:
            print(f"Asignando WIP limit {DEFAULT_WIP_LIMITS[name]} a {params['name']}")
            if not set_wip_limit(trello_list["id"], DEFAULT_WIP_LIMITS[name]):
                print(
                    "Trello no acepto el softLimit visual; "
                    "el limite duro se mantiene en el script."
                )

        lists[name] = trello_list["id"]

    return lists


def create_labels(board_id, rows):
    label_names = sorted({label for row in rows for label in labels_from(row)})
    labels = {}

    for index, name in enumerate(label_names):
        print(f"Creando label: {name}")
        label = trello("POST", f"/boards/{board_id}/labels", {
            "name": name,
            "color": LABEL_COLORS[index % len(LABEL_COLORS)],
        })
        labels[name] = label["id"]

    return labels


def create_cards(rows, list_name, list_id, labels):
    for row in rows:
        title = row["Titulo"].strip()
        card_label_ids = [labels[label] for label in labels_from(row) if label in labels]
        params = {
            "idList": list_id,
            "name": title,
            "desc": card_description(row),
        }

        if card_label_ids:
            params["idLabels"] = ",".join(card_label_ids)

        print(f"Creando tarjeta: {title}")
        enforce_wip_limit(list_name, list_id)
        trello("POST", "/cards", params)


def main():
    rows = read_rows()
    print(f"User stories leidas: {len(rows)}")

    delete_existing_boards()
    board = create_board()
    lists = create_lists(board["id"])
    labels = create_labels(board["id"], rows)
    create_cards(rows, INITIAL_LIST, lists[INITIAL_LIST], labels)
    validate_wip_limits(lists)

    print("Tablero Trello poblado.")
    print(board["url"])


if __name__ == "__main__":
    main()
