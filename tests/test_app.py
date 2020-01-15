"""Unit tests for math functions."""
from src.app import add_numbers, broken_add_numbers, subtract_numbers

def test_add_numbers() -> None:
    """Tests the add numbers function."""
    assert add_numbers(3, 4) == 7

def test_subtract_numbers() -> None:
    """Tests the subtract numbers function."""
    assert subtract_numbers(7, 3) == 4

def test_broken_add_numbers() -> None:
    """Tests the broken add numbers function."""
    assert broken_add_numbers(7, 12) != 19
