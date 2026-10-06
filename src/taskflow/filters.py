from __future__ import annotations

from .models import Task


def paginate(items: list, page: int, size: int) -> list:
    """1-based пагинация. page=1 — первая страница."""
    # BUG #1: off-by-one — должно быть (page - 1) * size
    start = page * size
    return items[start : start + size]


def search_by_title(tasks: list[Task], query: str) -> list[Task]:
    """Регистронезависимый поиск по подстроке в title."""
    # BUG #2: поиск регистрозависимый
    return [t for t in tasks if query in t.title]


def filter_by_tags(tasks: list[Task], tags: list[str]) -> list[Task]:
    """Возвращает задачи, содержащие ВСЕ переданные теги."""
    # BUG #3: используется any вместо all
    return [t for t in tasks if any(tag in t.tags for tag in tags)]


def sort_by_priority(tasks: list[Task]) -> list[Task]:
    """Сортировка по priority по убыванию."""
    # BUG #4: сортировка по возрастанию
    return sorted(tasks, key=lambda t: t.priority)