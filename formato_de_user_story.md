# US-01 | Feature: Implementar login de usuario

## Descripción

Actualmente los usuarios registrados no pueden iniciar sesión en la aplicación.  
Se necesita implementar un formulario de login conectado al backend para permitir el acceso seguro al sistema.

**Como** usuario registrado,  
**quiero** iniciar sesión con mi email y contraseña,  
**para** acceder a mi cuenta y usar la aplicación.

## Referencias visuales

Por definir

## Criterios de aceptación en formato test cases

- [ ] TC-01: Login exitoso con credenciales válidas
- [ ] TC-02: Login fallido con credenciales inválidas
- [ ] TC-03: Validación de campos obligatorios
- [ ] TC-04: Botón deshabilitado durante carga
- [ ] TC-05: Redirección al home después del login
- [ ] TC-06: Permanencia en login cuando ocurre un error

## Tareas

### Backend

- [ ] BE-01: Crear endpoint `POST /api/login`
- [ ] BE-02: Validar email y contraseña
- [ ] BE-03: Retornar token o sesión
- [ ] BE-04: Manejar errores de credenciales inválidas

### Frontend

- [ ] FE-01: Crear formulario de login
- [ ] FE-02: Conectar formulario con `/api/login`
- [ ] FE-03: Manejar estado de carga
- [ ] FE-04: Mostrar errores de validación
- [ ] FE-05: Redirigir al home después del login exitoso

## Estimación del esfuerzo (story points)

5

## Prioridad

Alta

## Etiquetas (labels)

login
