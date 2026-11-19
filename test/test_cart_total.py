import pytest
from src.cart_total import calculate_total


def test_one_item():
    result = calculate_total(350, 1)
    assert result == 350
    assert type(result) is int


def test_multiple_items():
    assert calculate_total(125, 8) == 1000


def test_zero_price():
    assert calculate_total(0, 5) == 0


def test_zero_quantity():
    assert calculate_total(250, 0) == 0


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total(-1, 2)


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_total(100, -1)


def test_string_price():
    with pytest.raises(TypeError):
        calculate_total("100", 2)


def test_string_quantity():
    with pytest.raises(TypeError):
        calculate_total(100, "2")


def test_none_price():
    with pytest.raises(TypeError):
        calculate_total(None, 2)


def test_none_quantity():
    with pytest.raises(TypeError):
        calculate_total(100, None)


def test_float_price():
    with pytest.raises(TypeError):
        calculate_total(1.5, 2)


def test_float_quantity():
    with pytest.raises(TypeError):
        calculate_total(100, 1.5)


def test_true_price():
    with pytest.raises(TypeError):
        calculate_total(True, 2)


def test_false_price():
    with pytest.raises(TypeError):
        calculate_total(False, 2)


def test_true_quantity():
    with pytest.raises(TypeError):
        calculate_total(100, True)


def test_false_quantity():
    with pytest.raises(TypeError):
        calculate_total(100, False)