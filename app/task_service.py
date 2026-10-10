from datetime import datetime, timezone

from .errors import ValidationError
from .validators import VALID_PRIORITIES

_tasks = {}
_next_id = 1


def reset():
    global _next_id
    _tasks.clear()
    _next_id = 1


def create_task(title, priority="medium", due_date=None, owner_id=None):
    global _next_id
    title = (title or "").strip()
    if not title:
        raise ValidationError("title is required")
    if priority not in VALID_PRIORITIES:
        raise ValidationError("invalid priority")
    if due_date is not None:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValidationError("due_date must be YYYY-MM-DD")
    task = {
        "id": _next_id,
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "owner_id": owner_id,
        "status": "open",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "completed_at": None,
    }
    _tasks[_next_id] = task
    _next_id += 1
    return task


def get_task(task_id):
    task = _tasks.get(task_id)
    # TODO: raise TaskNotFoundError when the task does not exist
    #       (the API layer should map it to a 404 response)
    return task


def list_tasks(status=None):
    tasks = list(_tasks.values())
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    return tasks


def search_tasks(query):
    q = query.lower()
    return [t for t in _tasks.values() if q in t["title"].lower()]


def complete_task(task_id):
    task = _tasks[task_id]
    # EDGE CASE: completing an already-completed task must be a no-op.
    # Keep the original completed_at, return the task unchanged (HTTP 200).
    task["status"] = "done"
    task["completed_at"] = datetime.now(timezone.utc).isoformat()
    return task
