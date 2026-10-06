from __future__ import annotations

from .models import Task


class InMemoryStorage:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, task: Task) -> Task:
        if task.id == 0:
            task.id = self._next_id
            self._next_id += 1
        self._tasks[task.id] = task
        return task

    def get(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def all(self) -> list[Task]:
        return list(self._tasks.values())

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None