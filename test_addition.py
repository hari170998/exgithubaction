import pytest
from addition import add


def test_add_two_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -4) == -5


def test_add_zero():
    assert add(0, 10) == 10
