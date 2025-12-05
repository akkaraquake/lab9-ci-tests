import pytest
from calculator import Calculator

calculator = Calculator()


# ---------- Тесты для add ----------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, -2, -3),
        (-1, 2, 1),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_add(a, b, expected):
    assert calculator.add(a, b) == expected


# ---------- Тесты для divide ----------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 2, 2),
        (5, 2, 2.5),
        (-6, 3, -2),
        (0, 5, 0),
    ],
)
def test_divide_normal(a, b, expected):
    assert calculator.divide(a, b) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)


# ---------- Тесты для is_prime_number ----------

@pytest.mark.parametrize(
    "n, expected",
    [
        (-10, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (10, False),
        (11, True),
        (25, False),
    ],
)
def test_is_prime_number(n, expected):
    assert calculator.is_prime_number(n) == expected
