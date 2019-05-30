from simple_calculator_tdd import add

def test_add():
	result = add(0,0)
	assert result == 0

def test_add_negatives():
	result = add(-1,-1)
	assert result == -2


def test_add_positives():
	result = add(4,5)
	assert result == 9
def test_many_numbers():
	result = add(1,2,3,4)
	assert result == 10

def test_multiply():
	result = 1*2
	assert result == 2

def test_multiply_many_numbers():
	result = 1*2*3*4
	assert result == 24