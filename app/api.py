from . import task_service, user_service
from .errors import ValidationError


# ---- users ----
def users_create(payload):
    try:
        user = user_service.create_user(payload.get("username"), payload.get("email"))
    except ValidationError as e:
        return 400, {"error": str(e)}
    return 201, {"data": user}


def users_get(user_id):
    user = user_service.get_user(user_id)
    if user is None:
        return 404, {"message": "not found"}
    return 200, {"data": user}


# ---- tasks ----
def tasks_create(payload):
    try:
        task = task_service.create_task(
            payload.get("title"),
            payload.get("priority", "medium"),
            payload.get("due_date"),
            payload.get("owner_id"),
        )
    except ValidationError as e:
        return 400, {"errors": [str(e)]}
    return 200, task


def tasks_get(task_id):
    task = task_service.get_task(task_id)
    return 200, task


def tasks_list(params):
    return 200, task_service.list_tasks(params.get("status"))


def tasks_search(params):
    return 200, task_service.search_tasks(params.get("q", ""))


def tasks_complete(task_id):
    try:
        return 200, task_service.complete_task(task_id)
    except KeyError:
        return 400, {"detail": "bad task id"}
