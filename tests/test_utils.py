from datetime import datetime

import pytest

from taskflow import utils


def test_email_valid():
    assert utils.is_valid_email("user@example.com")


def test_email_missing_dot_in_domain():
    assert not utils.is_valid_email("a@b")


def test_email_no_at():
    assert not utils.is_valid_email("not-an-email")


def test_add_month_regular():
    assert utils.add_month(datetime(2024, 5, 15)) == datetime(2024, 6, 15)


def test_add_month_december():
    assert utils.add_month(datetime(2024, 12, 15)) == datetime(2025, 1, 15)


def test_truncate_ascii():
    assert utils.truncate("hello world", 5) == "hello"


def test_truncate_cyrillic():
    # 6 символов, обрезаем до 3 — ожидаем ровно 3 символа
    assert utils.truncate("привет", 3) == "при"


def test_truncate_shorter_than_n():
    assert utils.truncate("hi", 10) == "hi"


def test_clamp_below():
    assert utils.clamp(-5, 0, 100) == 0


def test_clamp_above():
    assert utils.clamp(150, 0, 100) == 100


def test_clamp_inside():
    assert utils.clamp(50, 0, 100) == 50