import pytest

# Simple function to test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Example test functions
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(3, 5) == -2

# Example of parameterized test
@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected

# Example of a fixture
@pytest.fixture
def sample_data():
    return {"name": "pytest", "type": "testing"}

# Example test using a fixture
def test_using_fixture(sample_data):
    assert sample_data["name"] == "pytest"
    assert sample_data["type"] == "testing"
