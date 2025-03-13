from calculator import Calculator

import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_sum_pos_nums(calculator):
    assert calculator.add(1, 2) == 3

def test_sum_neg_nums(calculator):
    assert calculator.add(-1, -2) == -3