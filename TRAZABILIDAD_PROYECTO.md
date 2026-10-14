# Trazabilidad del proyecto: lo que tengo vs. lo que falta

## 1. Alcance y objetivo
Este documento permite comparar el estado actual del repositorio con los requisitos declarados en [AGENTS.md](AGENTS.md).

Leyenda:
- Estado: `Implementado`, `Parcial`, `Faltante`, `No aplica`
- Evidencia: archivo o fragmento que demuestra el estado actual

---

## 2. Resumen ejecutivo
El proyecto actual es una API mínima de ejemplo basada en FastAPI y SQLAlchemy, con un modelo simple de `ProductModel` y una ruta base de eventos.

No coincide todavía con la arquitectura del proyecto Enexia descrita en [AGENTS.md](AGENTS.md): faltan módulos de autenticación, seguridad, usuarios, eventos, reglas de negocio, validación de profanidad, base de datos real y pruebas automatizadas.

---

## 3. Matriz de trazabilidad

| Requisito / bloque | Estado | Evidencia actual | Comentario |
|---|---|---|---|
| Stack base: Python 3.11+, FastAPI, SQLAlchemy, Pydantic v2 | Parcial | `requirements.txt`, `app/main.py`, `app/models/products.py` | Hay FastAPI y SQLAlchemy, pero no se ve Pydantic v2 explícito ni una configuración clara del proyecto. |
| App principal creada | Implementado | `app/main.py` | Existe una instancia de `FastAPI()`. |
| Modelo de productos | Implementado | `app/models/products.py` | Hay una entidad `ProductModel` con `id`, `nombre`, `precio`, `stock`. |
| Router de productos/eventos | Parcial | `app/routers/products.py` | Hay un router con prefijo `/events`, pero no corresponde a la estructura pedida por el proyecto. |
| Schemas Pydantic | Parcial | `app/schemas.py` | Existe un `Evento` con validación básica, pero no hay DTOs del dominio del sistema real. |
| Configuración de BD | Parcial | `cfg/database.py` | Hay configuración de engine y sessionmaker, pero no se usan variables de entorno ni la estructura esperada. |
| Configuración general | Faltante | `cfg/config.py` | El archivo está vacío. |
| Módulo `app/core` | Faltante | No existe | Faltan config, security, JWT, hashing, session. |
| Módulo `app/models` de usuarios/personas/eventos | Faltante | Solo está `products.py` | No existe el modelo de negocio del sistema real. |
| Módulo `app/schemas` con DTOs | Faltante | Hay `app/schemas.py` pero no es el esquema del sistema | Es una entidad de ejemplo, no los DTOs de auth/eventos/usuarios. |
| Módulo `app/routers` con auth/events | Faltante | Solo existe `products.py` | No hay endpoints de login, registro, eventos ni permisos. |
| Módulo `app/services` | Faltante | No existe | Faltan servicios de negocio. |
| Seguridad JWT / Password hashing | Faltante | No existe | No hay `passlib`, `PyJWT` ni hashing BCrypt. |
| Validación de profanity | Faltante | No existe | No hay `better-profanity` ni validaciones. |
| Login silencioso / bloqueo por intentos | Faltante | No existe | No hay flow de identidad, cuenta, bloqueo ni política 401 uniforme. |
| Registro de Persona Física + Usuario | Faltante | No existe | No hay alta de usuario con rol y validación. |
| Gestión de eventos | Faltante | No existe | No hay pipeline de estados, moderación ni borrado lógico. |
| Frontend estático en `/static` | Faltante | No existe | No hay frontend ni archivos HTML/CSS/JS. |
| Pruebas automatizadas | Faltante | No hay carpeta `tests/` | No hay `pytest` ni casos de prueba. |
| Migraciones Alembic | Faltante | No hay `alembic` ni configuración | No hay migraciones ni setup de base de datos. |
| Base de datos MySQL/MariaDB real | Parcial | `cfg/database.py` | Usa una URL con MySQL, pero no está configurada con la convención del proyecto. |
| Borrado lógico | Faltante | No existe | No hay `fecha_baja` ni control de eliminación lógica. |
| Doble eje de estados de eventos | Faltante | No existe | No hay `estado_organizador` ni `estado_sistema`. |

---

## 4. Estado por área funcional

### 4.1 Infraestructura
- Estado: `Parcial`
- Lo que hay: FastAPI, SQLAlchemy, configuraciones básicas.
- Lo que falta: estructura de proyecto según AGENTS, variables de entorno, seguridad, app core, base de datos real.

### 4.2 Autenticación y usuarios
- Estado: `Faltante`
- Lo que falta: login por nickname, hashing con BCrypt, JWT, bloqueo por 3 fallos, email de notificación, manejo silencioso de credenciales inválidas.

### 4.3 Eventos
- Estado: `Faltante`
- Lo que falta: permisos de organizador, pipeline de moderación, validación de profanidad, borrado lógico.

### 4.4 Frontend
- Estado: `Faltante`
- Lo que falta: archivos HTML/CSS/JS servidos desde `/static` y acceso bajo `http://localhost:8000/`.

### 4.5 Calidad y validación
- Estado: `Faltante`
- Lo que falta: pruebas con `pytest`, validación de comportamiento, verificaciones contra invariantes del sistema.

---

## 5. Conclusión
El repositorio actual es un proyecto base de ejemplo, no una implementación del sistema Enexia descrito en [AGENTS.md](AGENTS.md).

El backlog mínimo que debería resolverse para alinear el proyecto es:
1. Reestructurar la app con `app/core`, `app/models`, `app/schemas`, `app/routers`, `app/services`.
2. Implementar autenticación real con usuarios, roles y bloqueo silencioso.
3. Modelar eventos con estados, permisos y moderación.
4. Completar frontend y tests.
5. Dejar la configuración de base de datos y entorno acorde a la arquitectura del sistema.

---

## 6. Archivos relevantes revisados
- `app/main.py`
- `app/models/products.py`
- `app/routers/products.py`
- `app/schemas.py`
- `cfg/database.py`
- `cfg/config.py`
- `requirements.txt`
- `AGENTS.md`

---

## 7. Sugerencia de próximo paso
Se recomienda transformar este documento en una checklist de implementación por módulos y luego ir marcando cada item como `Hecho / En progreso / Pendiente` durante el desarrollo.
