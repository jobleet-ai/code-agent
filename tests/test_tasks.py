import pytest

from app import task_service, user_service
from app.errors import ValidationError


@pytest.fixture(autouse=True)
def _clean():
    task_service.reset()
    user_service.reset()


def test_create_task_defaults():
    t = task_service.create_task("Write docs")
    assert t["priority"] == "medium"
    assert t["status"] == "open"


def test_title_required():
    with pytest.raises(ValidationError):
        task_service.create_task("   ")


def test_complete_task():
    t = task_service.create_task("Ship it")
    assert task_service.complete_task(t["id"])["status"] == "done"


def test_create_user():
    u = user_service.create_user("alice1", "a@example.com")
    assert u["id"] == 1
