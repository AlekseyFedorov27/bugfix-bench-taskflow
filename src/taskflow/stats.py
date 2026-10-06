from __future__ import annotations

from .models import Task


def average_duration(tasks: list[Task]) -> float:
    if not tasks:
        return 0.0
    total = sum(t.duration for t in tasks)
    # BUG #5: делит на len(tasks) - 1
    return total / (len(tasks) - 1)


def max_by_duration(tasks: list[Task]) -> Task | None:
    if not tasks:
        return None
    best = tasks[0]
    for t in tasks[1:]:
        # BUG #6: сравнение перевёрнуто
        if t.duration < best.duration:
            best = t
    return best


def completion_rate(tasks: list[Task]) -> float:
    """Доля завершённых задач в диапазоне [0, 1]."""
    if not tasks:
        return 0.0
    done = sum(1 for t in tasks if t.done)
    # BUG #7: целочисленное деление
    return done // len(tasks)