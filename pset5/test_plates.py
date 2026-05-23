from plates import is_valid

def test_valid_plates():
    assert is_valid("AA") is True
    assert is_valid("CS50") is True
    assert is_valid("ECTO88") is True

def test_invalid_length():
    assert is_valid("A") is False
    assert is_valid("OUTATIME") is False

def test_invalid_start():
    assert is_valid("50CS") is False
    assert is_valid("C50") is False

def test_invalid_number_placement():
    assert is_valid("CS50P") is False
    assert is_valid("AAA22A") is False

def test_zero_placement():
    assert is_valid("CS05") is False

def test_punctuation_and_spaces():
    assert is_valid("PI3.14") is False
    assert is_valid("CS 50") is False
