from __future__ import annotations

import re
from datetime import datetime

# BUG #9: слишком слабый regex
EMAIL_RE = re.compile(r".+@.+")


def is_valid_email(s: str) -> bool:
    """Валидный email требует точку в домене."""
    return bool(EMAIL_RE.fullmatch(s))


def add_month(dt: datetime) -> datetime:
    """Прибавить один календарный месяц."""
    # BUG #10: падает на декабре
    return dt.replace(month=dt.month + 1)


def truncate(s: str, n: int) -> str:
    """Обрезать строку до n СИМВОЛОВ."""
    # BUG #11: режет по байтам utf-8
    return s.encode("utf-8")[:n].decode("utf-8", errors="ignore")


def clamp(x: float, lo: float, hi: float) -> float:
    """Ограничить x в [lo, hi]."""
    if x < lo:
        return lo
    # BUG #12: должно быть x > hi
    if x < hi:
        return hi
    return x