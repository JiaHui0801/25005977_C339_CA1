import pytest
from src.cart_delivery import qualifies_free_delivery

def test_qualifies_free_delivery():
    assert qualifies_free_delivery(100) == False
    assert qualifies_free_delivery(200) == False
    assert qualifies_free_delivery(50) == False

def test_qualifies_free_delivery_zero():
    assert qualifies_free_delivery(0) == False

def test_qualifies_free_delivery_string():
    with pytest.raises(TypeError):
        qualifies_free_delivery("100")

def test_qualifies_free_delivery_none():
    with pytest.raises(TypeError):
        qualifies_free_delivery(None)

def test_qualifies_free_delivery_list():
    with pytest.raises(TypeError):
        qualifies_free_delivery([100])

def test_qualifies_free_delivery_dict():
    with pytest.raises(TypeError):
        qualifies_free_delivery({"amount": 100})

def test_qualifies_free_delivery_tuple():
    with pytest.raises(TypeError):
        qualifies_free_delivery((100,))

def test_free_delivery_just_below_minimum():
    assert qualifies_free_delivery(4999) is False

def test_free_delivery_at_5000():
    assert qualifies_free_delivery(5000) is True

def test_free_delivery_just_above_minimum():
    assert qualifies_free_delivery(5001) is True

def test_free_delivery_large_order():
    assert qualifies_free_delivery(10000) is True