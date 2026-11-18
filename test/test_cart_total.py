import pytest
from src.cart_total import calculate_total

def test_calculate_total_zero():
    assert calculate_total(0, 0) == 0

def test_calculate_total_negative():
    with pytest.raises(ValueError):
        calculate_total(-100, -10)

def test_calculate_total_string():
    with pytest.raises(TypeError):
        calculate_total("100", "10")

def test_calculate_total_none():
    with pytest.raises(TypeError):
        calculate_total(None, None)

def test_calculate_total_list():
    with pytest.raises(TypeError):
        calculate_total([100], [10])

def test_calculate_total_dict():
    with pytest.raises(TypeError):
        calculate_total({"amount": 100}, {"tax": 10})

def test_calculate_total_tuple():
    with pytest.raises(TypeError):
        calculate_total((100,), (10,))

def test_cart_total_one_item():
    assert calculate_total(350, 1) == 350


def test_cart_total_multiple_items():
    assert calculate_total(125, 8) == 1000

def test_cart_total_free_items():
    assert calculate_total(0, 5) == 0

def test_zero_quantity():
    assert calculate_total(250, 0) == 0