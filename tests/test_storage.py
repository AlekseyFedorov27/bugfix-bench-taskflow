from taskflow.models import Task
from taskflow.storage import InMemoryStorage


def test_add_assigns_id():
    s = InMemoryStorage()
    t = s.add(Task(id=0, title="a"))
    assert t.id == 1


def test_add_increments_id():
    s = InMemoryStorage()
    a = s.add(Task(id=0, title="a"))
    b = s.add(Task(id=0, title="b"))
    assert (a.id, b.id) == (1, 2)


def test_delete():
    s = InMemoryStorage()
    t = s.add(Task(id=0, title="a"))
    assert s.delete(t.id) is True
    assert s.get(t.id) is None


def test_delete_missing():
    s = InMemoryStorage()
    assert s.delete(999) is False