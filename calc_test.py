import sys

from calculator import Calculator

import pytest

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize('num1, num2, result', [
    (4, 5, 9),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 3.5, 6.0),
])
def test_sum_nums(calculator, num1, num2, result):
    res = calculator.add(num1, num2)
    assert res == result

@pytest.mark.skip(reason="Тест отключен")
def test_sum_neg_nums(calculator):
    assert calculator.add(-1, -2) == -3

@pytest.mark.skipif(condition='sys.version_info < (3, 8)', reason="требуется Python 3.8")
def test_div_by_zero(calculator):
    with pytest.raises(ArithmeticError, match="На ноль делить нельзя"):
        calculator.divide(10, 0)
@pytest.mark.user_marker
def test_mul_pos_nums(calculator):
    assert calculator.multiply(2, 2) == 4