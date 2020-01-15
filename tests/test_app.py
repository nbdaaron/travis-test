from src.app import add_numbers, subtract_numbers

def setup():
    pass

def teardown():
    pass

def test_add_numbers():
    assert add_numbers(3,4) == 7

def test_subtract_numbers():
	assert subtract_numbers(7,3) == 4