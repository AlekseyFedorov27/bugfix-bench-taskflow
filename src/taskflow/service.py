from __future__ import annotations

from .models import Task
from .storage import InMemoryStorage


class TaskService:
    def __init__(self, storage: InMemoryStorage) -> None:
        self.storage = storage

    def create_task(self, title: str, tags: list[str] = []) -> Task:
        # BUG #8: mutable default argument
        tags.append("new")
        task = Task(id=0, title=title, tags=tags)
        return self.storage.add(task)

    def complete(self, task_id: int) -> Task | None:
        task = self.storage.get(task_id)
        if task is None:
            return None
        task.done = True
        return task

    def rename(self, task_id: int, new_title: str) -> Task | None:
        task = self.storage.get(task_id)
        if task is None:
            return None
        task.title = new_title
        return task