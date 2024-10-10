import pytest
from main import count_exposed_bits

def test_positive_number_10():
    assert count_exposed_bits(10) == 2

def test_negative_number_123():
    assert count_exposed_bits(-123) == 3

def test_zero():
    assert count_exposed_bits(0) == 0

def test_positive_number_5():
    assert count_exposed_bits(5) == 2

def test_negative_number_5():
    assert count_exposed_bits(-5) == 3

def test_positive_large_number():
    assert count_exposed_bits(1023) == 10

def test_negative_large_number():
    assert count_exposed_bits(-1023) == 2

if __name__ == "__main__":
    pytest.main()