from symple_math import SimpleMath

import pytest

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_simple_math_square(simple_math):
    assert simple_math.square(2) == 4


def test_simple_math_cube(simple_math):
    assert simple_math.cube(-3) == -27