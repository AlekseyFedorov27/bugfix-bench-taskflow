Issue #1 — paginate возвращает не ту страницу
Метки: bug, module:filters, difficulty:easy

Воспроизведение:

python
from taskflow import filters
filters.paginate(list(range(1, 11)), page=1, size=3)  # ждали [1,2,3]
Ожидалось: [1, 2, 3] — page нумеруется с 1.
Фактически: [4, 5, 6].

Тесты, падающие сейчас: tests/test_filters.py::test_paginate_first_page, ::test_paginate_second_page, ::test_paginate_last_page_partial.

Issue #2 — search_by_title учитывает регистр
Метки: bug, module:filters, difficulty:easy

Воспроизведение:

python
from taskflow import filters
from taskflow.models import Task
tasks = [Task(id=1, title="Fix Login Bug")]
filters.search_by_title(tasks, "login")  # ждали [Task(1)]
Ожидалось: поиск без учёта регистра.
Фактически: пустой список.

Тесты: test_search_case_insensitive.

Issue #3 — filter_by_tags возвращает OR вместо AND
Метки: bug, module:filters, difficulty:easy

Ожидалось: задачи, у которых есть все теги.
Фактически: достаточно одного тега.

Тесты: test_filter_by_tags_requires_all.

Issue #4 — sort_by_priority сортирует по возрастанию
Метки: bug, module:filters, difficulty:easy

Ожидалось: по убыванию priority.
Фактически: по возрастанию.

Тесты: test_sort_by_priority_desc.

Issue #5 — average_duration делит на len - 1
Метки: bug, module:stats, difficulty:medium

Ожидалось: среднее по всем задачам.
Фактически: [10, 20] → 30.0 (вместо 15.0), а на одной задаче — ZeroDivisionError.

Тесты: test_average_duration_two_tasks, test_average_duration_single_task.

Issue #6 — max_by_duration возвращает минимум
Метки: bug, module:stats, difficulty:easy

Ожидалось: задача с максимальной duration.
Фактически: с минимальной.

Тесты: test_max_by_duration.

Issue #7 — completion_rate использует целочисленное деление
Метки: bug, module:stats, difficulty:easy

Ожидалось: 0.5 для 1 из 2.
Фактически: 0.

Тесты: test_completion_rate_half, test_completion_rate_all_done.

Issue #8 — mutable default в TaskService.create_task
Метки: bug, module:service, difficulty:medium

Воспроизведение:

python
svc = TaskService(InMemoryStorage())
t1 = svc.create_task("a")
t2 = svc.create_task("b")
t2.tags  # ['new', 'new']
Ожидалось: у каждой задачи свой список тегов, ['new'].
Фактически: теги накапливаются между вызовами.

Тесты: test_create_task_does_not_leak_tags.

Issue #9 — is_valid_email пропускает email без точки в домене
Метки: bug, module:utils, difficulty:easy

Ожидалось: is_valid_email("a@b") is False.
Фактически: True.

Тесты: test_email_missing_dot_in_domain.

Issue #10 — add_month падает на декабре
Метки: bug, module:utils, difficulty:medium

Воспроизведение:

python
utils.add_month(datetime(2024, 12, 15))  # ValueError
Ожидалось: datetime(2025, 1, 15).
Фактически: ValueError: month must be in 1..12.

Тесты: test_add_month_december.

Issue #11 — truncate режет по байтам, а не по символам
Метки: bug, module:utils, difficulty:medium

Ожидалось: truncate("привет", 3) == "при".
Фактически: "п" (или ломаный utf-8).

Тесты: test_truncate_cyrillic.

Issue #12 — clamp неправильно обрабатывает x > hi
Метки: bug, module:utils, difficulty:easy

Ожидалось: clamp(150, 0, 100) == 100.
Фактически: 150.

Тесты: test_clamp_above.

