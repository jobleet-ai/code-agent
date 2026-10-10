# TaskFlow

A tiny in-memory task manager used as a demo codebase.
There is no web framework: "endpoints" in `app/api.py` are plain functions
that return `(status_code, body)`.

## Layout
- `app/user_service.py` - user CRUD
- `app/task_service.py` - task CRUD, search, completion
- `app/api.py` - endpoint functions
- `app/validators.py`, `app/errors.py`, `app/utils.py`, `app/config.py`
- `legacy/` - old scripts, not part of the app
- `tests/` - pytest suite (`python -m pytest`)

## Task validation rules
- `title`: required, stripped, 1-100 characters
- `priority`: one of `low`, `medium`, `high` (default `medium`)
- `due_date`: optional, ISO format `YYYY-MM-DD`, must not be in the past

## API status codes
| Situation                     | Code |
|-------------------------------|------|
| Resource created              | 201  |
| Success                       | 200  |
| Validation failure            | 422  |
| Resource not found            | 404  |
| Conflict (e.g. duplicate)     | 409  |
