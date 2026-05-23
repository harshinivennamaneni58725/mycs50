from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0

def test_starts_with_h():
    assert value("hey") == 20
    assert value("How you doing?") == 20

def test_other_greetings():
    assert value("What's up?") == 100
    assert value("good morning") == 100
