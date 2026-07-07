Usando el formato de user story definido dentro de formato_de_user_story.md crea un archivo user_stories.csv con 15 issues como Product Backlog para un MVP v1.0 definido dentro [mvp] y desarrollado con SCRUM de 4 sprints y sprints de una semana.

Considera el contexto de proyecto definido dentro de [contexto], con prototipo UI que sigue EXACTAMENTE la arquitectura de información definida dentro de [arquitectura], y alineado con la protopersona descrita dentro de en [protopersona] para completar el taskflow dentro de [taskflow].

## REGLAS OBLIGATORIAS

Las columnas del CSV deben ser:

- Titulo
- Descripción
- Referencias visuales
- Criterios de aceptación en formato test cases
- Tareas
- Estimación del esfuerzo (story points)
- Prioridad
- Etiquetas (labels)

Las tareas deben ser varias técnicas con términos técnicos porque las realizarán SCRUM developers:

| Nombre del rol         | Abreviatura |
| ---------------------- | ----------- |
| Frontend Developer     | FE          |
| Backend Developer      | BE          |
| Quality Assurance      | QA          |
| UX/UI Designer         | UX          |
| DevOps Engineer        | DEVOPS      |
| Database Administrator | DB          |
| Security Engineer      | SEC         |
| Cloud Engineer         | CLD         |
| Technical Writer       | DOC         |
| Mobile Developer       | MOB         |

## MVP

[mvp]

# MVP v1.0

## Descripción

El MVP v1.0 es una versión simple del sistema de seguimiento post-venta para TechFin Perú.

Se desarrolla en 4 sprints de 1 semana cada uno. En esta versión solo se trabaja el registro de clientes y la generación de alertas.

## Qué debe tener

- Registro básico de clientes.
- Lista básica de clientes.
- Ficha básica del cliente.
- Lista de alertas de recompra.
- Datos de prueba con clientes existentes y compras anteriores.

## Resultado esperado

Al final de los 4 sprints debe existir una versión básica donde se puedan registrar clientes, ver clientes existentes y visualizar alertas de recompra.

[/mvp]

## CONTEXTO, PROTOPERSONA Y TASKFLOW:

[contexto]

Empresa: TechFin Perú S.A.C., empresa dedicada a la comercialización y distribución de productos tecnológicos (laptops, computadoras, accesorios y dispositivos electrónicos), orientada a ofrecer soluciones digitales integradas para optimizar la gestión comercial.

Proceso analizado: Ventas y seguimiento post-venta de clientes comerciales y corporativos, desde el registro del pedido en la plataforma web hasta el control de la relación post-venta desde el panel administrativo.

Problema central identificado en el avance anterior: Los encargados de ventas comerciales gestionan entre 15 y 30 clientes de forma simultánea. Al no contar con un sistema de seguimiento automatizado, dependen de su memoria y de hojas de cálculo para recordar cuándo contactar a cada cliente después de una venta. Esto genera una pérdida sistemática de oportunidades de recompra y up-selling, en especial en productos tecnológicos con ciclos de renovación y mantenimiento predecibles (laptops, equipos de cómputo, componentes de hardware).

Innovación propuesta: Implementar un módulo de alertas automáticas dentro de un sistema CRM integrado con la plataforma web, el cual notifique al encargado de ventas en el momento óptimo para contactar a cada cliente, calculadas automáticamente en función de la vida útil estimada o ciclo de renovación del producto tecnológico adquirido.

[/contexto]


[protopersona]

**Nombre y apellido:** Miqueas Lancho
**Rol / tipo de usuario:** Administrador Comercial / Encargado de Ventas de TechFin Perú S.A.C.
**Descripción del rol:** Responsable de supervisar el flujo de ventas generales, coordinar al equipo comercial, mantener actualizado el catálogo de productos y asegurar el control del seguimiento post-venta de los clientes de la empresa.
**Puntos de dolor:** Actualmente administra información dispersa entre mensajes, registros manuales y hojas de cálculo (Excel). Al no contar con un sistema centralizado, le resulta imposible supervisar si los vendedores están contactando a los clientes en el momento óptimo de renovación tecnológica, lo que genera retrasos, desorganización y una pérdida visible de ventas corporativas recurrentes.
**Necesidades:** Requiere un panel administrativo (Dashboard CRM) centralizado que no solo le permita ver las ventas, sino configurar los ciclos de vida de los productos tecnológicos para que el sistema genere las alertas automáticas. Necesita supervisar en tiempo real el estado de seguimiento de cada cliente asignado a su equipo para mejorar radicalmente la organización, la trazabilidad comercial y la efectividad de las recompras.

[/protopersona]

[taskflow]

**Taskflow 1:** Revisión y acción sobre una alerta de recompra urgente _(Happy Path)_

**Rol / tipo de usuario:** Encargado de Ventas Comerciales y Corporativas

**Objetivo del usuario dentro del sistema:** Identificar el cliente comercial o corporativo más urgente del día dentro del CRM de TechFin, revisar su contexto de hardware adquirido y registrar el resultado del contacto post-venta realizado sin desvíos ni errores.

1. Ingresa al CRM de TechFin Perú S.A.C.
2. Mira el Dashboard del Encargado de Ventas.
3. Mira el widget "Alertas de Recompra por Obsolescencia Tecnológica".
4. Identifica 2 alertas en rojo en el contador de clientes con equipos en estado "Crítico / Urgente" (ciclo de vida útil vencido).
5. Hace clic en la tarjeta de la primera alerta de renovación urgente.
6. Mira la Vista: Ficha del cliente comercial.
7. Lee la razón social de la empresa, el contacto clave, el lote de productos tecnológicos adquiridos, el monto y la fecha de la última compra.
8. Realiza la llamada telefónica de seguimiento al cliente fuera del sistema para ofrecer la renovación de los equipos.
9. Hace clic en el botón "Registrar contacto" dentro de la misma ficha.
10. Mira el Modal: Registro de Gestión Comercial.
11. Selecciona el resultado del contacto (ej. "Interesado en renovación/up-selling").
12. Escribe una nota detallada sobre la conversación y los requerimientos de hardware del cliente.
13. Confirma o edita la fecha programada para el próximo seguimiento comercial.
14. Hace clic en "Guardar y cerrar".
15. Mira el Dashboard del Encargado de Ventas con la alerta procesada correctamente y el contador de urgencias actualizado en tiempo real.

[/taskflow]

## ARQUITECTURA:

[arquitectura]

Vista: Dashboard del Encargado de Ventas Comerciales
    Sección: Barra superior
        Nombre del encargado activo
        Ícono: Notificaciones de alertas
        Ícono: Soporte y Ayuda
    Sección: Alertas de Recompra por Obsolescencia Tecnológica
        Contador: Equipos en estado Crítico (vencidas o con vencimiento hoy) -> Vista: Ficha del cliente comercial
        Contador: Renovaciones Próximas (1–7 días) -> Vista: Ficha del cliente comercial
        Contador: En Monitoreo / Seguimiento (8–30 días) -> Vista: Ficha del cliente comercial
        Tarjeta de Alerta de Hardware
            Razón Social de la empresa
            Lote / Producto de la última compra (ej. Laptops, Servidores)
            Monto del pedido anterior
            Días restantes para el fin de ciclo útil estimado
            Botón: Ver ficha técnica del cliente -> Vista: Ficha del cliente comercial
            Botón: Posponer alerta
    Sección: Agenda Comercial del Día
        Lista de llamadas y correos de seguimiento pendientes

Vista: Ficha del cliente comercial
    Enlace: Volver al Dashboard -> Vista: Dashboard del Encargado de Ventas Comerciales
    Razón Social de la empresa
    RUC (Registro Único de Contribuyentes)
    Contacto Principal de la Empresa
        Nombre del tomador de decisiones (ej. Jefe de TI / Compras)
        Teléfono / Correo institucional
    Encargado Comercial asignado (TechFin)
    Sección: Historial de la Última Adquisición Tecnológica
        Producto / Categoría de hardware
        Cantidad de unidades adquiridas
        Monto total de la transacción
        Fecha de cierre del pedido original
        Campo editable: Ciclo de vida útil estimado del producto (días)
        Fecha programada de alerta (calculada automáticamente)
    Sección: Bitácora e Historial de Notas del Encargado de Ventas
        Texto libre editable para incidencias o comentarios
    Sección: Acciones Comerciales
        Botón: Registrar gestión post-venta -> Modal: Registro de contacto comercial
        Botón: Posponer alerta de renovación (N días)
        Botón: Marcar como Sin oportunidad actual / Cuenta inactiva

Modal: Registro de contacto comercial
    Ícono: Cerrar modal
    Selector: Resultado de la gestión post-venta
        Opción: Interesado en renovación de hardware / Up-selling
        Opción: No interesado en este ciclo
        Opción: Cliente no contestó / Remitir correo
    Campo: Notas y detalles de la llamada
    Campo editable: Fecha del próximo contacto (default: fecha actual + ciclo de vida del equipo)
    Botón: Guardar gestión y cerrar
    Botón: Cancelar

Vista: Cartera de Clientes / Empresas
    Sección: Barra superior
        Nombre del encargado activo
        Ícono: Notificaciones
    Sección: Listado de Cuentas Comerciales
        Buscador por RUC o Razón Social
        Tarjeta de la Empresa
            Nombre comercial
            RUC
            Ejecutivo de cuentas asignado
            Enlace: Ver ficha técnica -> Vista: Ficha del cliente comercial

Vista: Pipeline de Ventas Corporativas
    Sección: Barra superior
        Nombre del encargado activo
    Sección: Tablero Kanban de Oportunidades
        Columna: Prospección / Lead Comercial
        Columna: Cotización de Hardware Enviada
        Columna: Evaluación de Crédito Comercial
        Columna: Venta Cerrada (Activa automáticamente el temporizador de ciclo de vida útil del hardware)
        Columna: Post-venta / Seguimiento Activo
        Tarjeta de Oportunidad de Negocio
            Razón Social de la empresa
            Monto proyectado de la venta
            Fecha estimada de cierre de negociación

Vista: Panel Gerencial / Dashboard de Supervisión
    Sección: Barra superior
        Nombre del Gerente Comercial activo
    Sección: Indicadores de Rendimiento (KPIs) del Equipo
        Contador: Alertas críticas de renovación vencidas sin acción comercial
        Contador: Contactos post-venta efectivos realizados en la semana
        Indicador (%): Tasa de conversión (Alerta de obsolescencia -> Nueva cotización de hardware)
    Sección: Filtros de Control
        Selector: Filtrar por ejecutivo de ventas de TechFin
        Selector: Filtrar por período de evaluación (Mensual/Trimestral)
    Sección: Matriz de Trazabilidad Comercial
        Fila por encargado de ventas
            Nombre del ejecutivo
            Alertas de obsolescencia ignoradas / vencidas
            Contactos comerciales registrados
            Porcentaje de efectividad en recompras

[/arquitectura]



