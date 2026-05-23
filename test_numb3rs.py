from pset7.numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True

def test_invalid_ip():
    assert validate("512.1.1.1") is False
    assert validate("1.2.3.1000") is False
    assert validate("cat") is False
