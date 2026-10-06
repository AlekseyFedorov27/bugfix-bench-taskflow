from taskflow.service import TaskService
from taskflow.storage import InMemoryStorage


def test_create_task_does_not_leak_tags():
    storage = InMemoryStorage()
    svc = TaskService(storage)
    t1 = svc.create_task("a")
    t2 = svc.create_task("b")

    assert t1.tags == ["new"]
    assert t2.tags == ["new"]

    t1.tags.append("x")
    assert "x" not in t2.tags


def test_complete():
    storage = InMemoryStorage()
    svc = TaskService(storage)
    t = svc.create_task("a")
    assert svc.complete(t.id).done is True


def test_rename():
    storage = InMemoryStorage()
    svc = TaskService(storage)
    t = svc.create_task("a")
    svc.rename(t.id, "b")
    assert storage.get(t.id).title == "b"