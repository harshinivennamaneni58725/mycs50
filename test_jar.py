import pytest
from jar import Jar


def test_init():
    jar = Jar(15)
    assert jar.capacity == 15
    with pytest.raises(ValueError):
        Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(4)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.withdraw(10)
