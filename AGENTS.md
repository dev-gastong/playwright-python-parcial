# AGENTS.md — Enexia (Python Engine)

## 1. Stack & Runtime
- **Backend:** Python 3.11+, FastAPI, SQLAlchemy (Async), Pydantic v2.
- **Seguridad:** Passlib (BCrypt, cost=12), PyJWT, better-profanity.
- **BD:** MySQL / MariaDB 10.6+ (`utf8mb4_unicode_ci`).
- **Frontend:** HTML5, CSS Vanilla, JS ES6+ (servido estáticamente en `/static` desde FastAPI, mismo origen `:8000`).

## 2. Comandos Operativos
- Instalar deps: `pip install -r requirements.txt`
- Ejecutar dev server: `uvicorn app.main:app --reload --port 8000`
- Correr tests: `pytest tests/ -v`
- Migraciones: `alembic upgrade head`

## 3. Estructura de Directorios
app/
├── core/          # Config, security (jwt, hashing), database session
├── models/        # Entidades SQLAlchemy (Usuario, Persona, Evento, etc.)
├── schemas/       # DTOs Pydantic (Request/Response)
├── routers/       # Endpoints REST (auth.py, events.py)
├── services/      # Lógica de negocio (auth_service, event_service)
└── static/        # Frontend Vanilla (HTML, CSS, JS)

## 4. Reglas Críticas del Sistema (Invariantes)

### MÓDULO 1: Auth & Registro (Login Silencioso)
1. **Identidad:** Todo `Usuario` pertenece estrictamente a una `Persona_Fisica` humana. El login es por `nickname`, NO por email.
2. **Registro PF:** Da de alta Persona Física + Usuario (`ACTIVO`). Rol asignado: `PARTICIPANTE` (u `ORGANIZADOR` + `PARTICIPANTE`).
3. **Filtro de Profanidad:** Validar nombre/nickname con `better-profanity` antes de persistir.
4. **Política de Bloqueo Silencioso (ADR-13):**
   - 3 fallos consecutivos en `usuario.intentos_fallidos` -> cuenta pasa a `BLOQUEADO`.
   - **Retorno HTTP idéntico (401 CREDENCIALES_INVALIDAS):** No revelar si el nickname no existe, si la contraseña falló o si la cuenta está bloqueada. Usar tiempo constante (BCrypt decoy hash si el usuario no existe).
   - En bloqueo: Notificar por email con token único; nunca alterar la respuesta HTTP.

### MÓDULO 2: Creación de Eventos
1. **Permisos:** Solo usuarios con rol `ORGANIZADOR` pueden crear eventos.
2. **Doble Eje de Estados:**
   - `estado_organizador`: Inicia en `PUBLICADO` o `BORRADOR`.
   - `estado_sistema`: Inicia en `EN_PROCESO` -> pasa a pipeline de moderación (`APROBADO_SISTEMA` / `RECHAZADO_SISTEMA`).
3. **Pipeline de Moderación:**
   - Validar texto de título y descripción con `better-profanity`.
   - Si no hay credenciales de Cloudinary (`CLOUDINARY_CLOUD_NAME` ausente), correr en modo simulado (archivos con nombre conteniendo `rechazar` se rechazan).
4. **Inmutabilidad y Borrado:** Usar borrado lógico (`fecha_baja`), nunca `DELETE` en base de datos.

## 5. Reglas de Código para el Agente
- Tipado estricto en Python (`typing`, `Pydantic`).
- No exponer entidades de base de datos en respuestas; mapear siempre a Pydantic Response schemas.
- No levantar servidores estáticos externos (LiveServer, http.server). Todo el frontend se accede bajo `http://localhost:8000/`.
- Antes de dar una tarea por finalizada, verificar que las pruebas pasen con `pytest`.