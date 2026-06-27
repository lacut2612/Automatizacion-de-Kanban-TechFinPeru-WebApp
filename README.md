# Automatizacion de Kanban en GitHub Projects

Este proyecto permite importar historias de usuario desde un archivo CSV y crear automaticamente:

- Un repositorio en GitHub.
- Issues a partir de las historias de usuario.
- Labels para los issues.
- Un GitHub Project tipo Kanban.
- Columnas como Product Backlog, To Do, In Progress, Testing y Done.
- Limites WIP en algunas columnas.

El archivo CSV usado por el script debe llamarse:

```txt
user_stories.csv
```

Este archivo puede ser generado usando el prompt:

```txt
create_user_stories.md
```

Ese prompt se puede ejecutar en una IA que viene con el IDE:

- Gemini Flash
- Claude Sonnet
- GitHub Copilot
- etc

La idea es pedirle a la IA que genere las historias de usuario en formato CSV y luego guardar el resultado como:

```txt
user_stories.csv
```

El script principal para importar Historias de Usuario en Github Projects es:

```bash
python import_user_stories_github_projects.py
```

Hay otro para crear uno en trello que es una opción alternativa.

---

## 1. Hacer fork del repositorio

Primero ingresa al repositorio original:

```txt
https://github.com/rgap/Automatizacion-de-Kanban-Coolbox-B2B-WebApp
```

Luego haz clic en:

```txt
Fork
```

GitHub creara una copia del repositorio en tu propia cuenta.

Por ejemplo, si tu usuario es `kravizt`, el repositorio forkeado quedaria parecido a:

```txt
https://github.com/kravizt/Automatizacion-de-Kanban-Coolbox-B2B-WebApp
```

---

## 2. Abrir el repositorio forkeado en Codespaces

Entra al repositorio que acabas de forkear.

Luego haz clic en:

```txt
Code > Codespaces > Create codespace on main
```

Esto abrira un entorno de desarrollo en la nube con el proyecto listo para ejecutarse.

---

## 3. Probar el script por primera vez

Dentro del Codespace, abre la terminal y ejecuta:

```bash
python import_user_stories_github_projects.py
```

El script leera las historias de usuario desde el archivo CSV.

Ejemplo de salida:

```txt
User stories leidas: 15
Creando repo: kravizt/Coolbox-B2B-WebApp
GraphQL: Resource not accessible by integration (createRepository)
```

---

## 4. ¿Por que aparece este error?

El error:

```txt
GraphQL: Resource not accessible by integration (createRepository)
```

ocurre porque Codespaces usa automaticamente una variable llamada `GITHUB_TOKEN`.

Ese token sirve para algunas operaciones basicas dentro del Codespace, pero no tiene permisos suficientes para crear repositorios, borrar repositorios o manejar GitHub Projects.

Por eso, aunque tengas sesion iniciada en GitHub, el comando `gh` puede estar usando el token limitado del entorno en vez de tus credenciales personales.

---

## 5. Solucion

Haz esto en la misma terminal del Codespace:

```bash
unset GITHUB_TOKEN
unset GH_TOKEN
```

Luego verifica el estado de autenticacion:

```bash
gh auth status
```

Despues refresca los permisos necesarios:

```bash
gh auth refresh -s repo,project,delete_repo
```

Si te pide iniciar sesion otra vez, ejecuta:

```bash
gh auth login
```

Luego vuelve a refrescar los permisos:

```bash
gh auth refresh -s repo,project,delete_repo
```

---

## 6. Ejecutar nuevamente el script

Finalmente corre otra vez:

```bash
python import_user_stories_github_projects.py
```

Ahora el script deberia poder crear el repositorio, los issues y el GitHub Project correctamente.

---

## 7. Permisos necesarios

El script necesita estos permisos:

| Permiso       | Para que sirve                                            |
| ------------- | --------------------------------------------------------- |
| `repo`        | Crear y editar repositorios, issues y labels              |
| `project`     | Crear y modificar GitHub Projects                         |
| `delete_repo` | Borrar el repositorio existente antes de volver a crearlo |

---

## 8. Nota importante

Este script puede borrar y volver a crear el repositorio configurado en el codigo.

Antes de ejecutarlo, revisa estas variables dentro de `import_user_stories_github_projects.py`:

```python
OWNER = "kravizt"
REPO = "Coolbox-B2B-WebApp"
FULL_REPO = f"{OWNER}/{REPO}"
```

Asegurate de que el `OWNER` sea tu usuario de GitHub y que el nombre del repositorio sea el que realmente quieres usar.
