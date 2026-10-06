from taskflow import stats
from taskflow.models import Task


def test_average_duration_two_tasks():
    tasks = [
        Task(id=1, title="a", duration=10),
        Task(id=2, title="b", duration=20),
    ]
    assert stats.average_duration(tasks) == 15.0


def test_average_duration_single_task():
    tasks = [Task(id=1, title="a", duration=10)]
    assert stats.average_duration(tasks) == 10.0


def test_average_duration_empty():
    assert stats.average_duration([]) == 0.0


def test_max_by_duration():
    tasks = [
        Task(id=1, title="a", duration=5),
        Task(id=2, title="b", duration=15),
        Task(id=3, title="c", duration=10),
    ]
    assert stats.max_by_duration(tasks).id == 2


def test_completion_rate_half():
    tasks = [
        Task(id=1, title="a", done=True),
        Task(id=2, title="b", done=False),
    ]
    assert stats.completion_rate(tasks) == 0.5


def test_completion_rate_all_done():
    tasks = [
        Task(id=1, title="a", done=True),
        Task(id=2, title="b", done=True),
    ]
    assert stats.completion_rate(tasks) == 1.0