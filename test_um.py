from pset7.um import count

def test_standalone():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_embedded():
    assert count("yummy") == 0
    assert count("bump") == 0

def test_multiple():
    assert count("um, hello, um, world") == 2
