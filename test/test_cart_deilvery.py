import pytest
from src.cart_delivery import qualifies_free_delivery


def test_zero_total():
    assert qualifies_free_delivery(0) is False


def test_below_delivery_minimum():
    assert qualifies_free_delivery(4999) is False


def test_at_delivery_minimum():
    assert qualifies_free_delivery(5000) is True


def test_above_delivery_minimum():
    assert qualifies_free_delivery(5001) is True


def test_negative_total():
    with pytest.raises(ValueError):
        qualifies_free_delivery(-1)


def test_string_total():
    with pytest.raises(TypeError):
        qualifies_free_delivery("5000")


def test_none_total():
    with pytest.raises(TypeError):
        qualifies_free_delivery(None)


def test_float_total():
    with pytest.raises(TypeError):
        qualifies_free_delivery(5000.0)


def test_true_total():
    with pytest.raises(TypeError):
        qualifies_free_delivery(True)


def test_false_total():
    with pytest.raises(TypeError):
        qualifies_free_delivery(False)