from taskflow import filters
from taskflow.models import Task


def test_paginate_first_page():
    items = list(range(1, 11))
    assert filters.paginate(items, page=1, size=3) == [1, 2, 3]


def test_paginate_second_page():
    items = list(range(1, 11))
    assert filters.paginate(items, page=2, size=3) == [4, 5, 6]


def test_paginate_last_page_partial():
    items = list(range(1, 8))
    assert filters.paginate(items, page=3, size=3) == [7]


def test_search_case_insensitive():
    tasks = [
        Task(id=1, title="Fix Login Bug"),
        Task(id=2, title="Add tests"),
    ]
    result = filters.search_by_title(tasks, "login")
    assert [t.id for t in result] == [1]


def test_filter_by_tags_requires_all():
    tasks = [
        Task(id=1, title="a", tags=["urgent", "backend"]),
        Task(id=2, title="b", tags=["urgent"]),
        Task(id=3, title="c", tags=["backend"]),
    ]
    result = filters.filter_by_tags(tasks, ["urgent", "backend"])
    assert [t.id for t in result] == [1]


def test_sort_by_priority_desc():
    tasks = [
        Task(id=1, title="a", priority=1),
        Task(id=2, title="b", priority=3),
        Task(id=3, title="c", priority=2),
    ]
    result = filters.sort_by_priority(tasks)
    assert [t.priority for t in result] == [3, 2, 1]