import math_functions


def test_add():
    assert math_functions.add(7, 3) == 10
    assert math_functions.add(3) == 5


def test_product():
    assert math_functions.product(4, 5) == 20
    assert math_functions.product(5) == 10
