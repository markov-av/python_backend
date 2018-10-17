import pytest
from lesson_4 import gcd


@pytest.mark.parametrize('test_input_n,test_input_m,expected', [
    (0, 2, 2),
    (100, 0, 100),
    (1, 1, 1),
    (1, 4, 1),
    (5, 1, 1),
    (10, 20, 10),
    (10, 11, 1),
    (11, 10, 1)
])
def test_gcd(test_input_n, test_input_m, expected):
    assert gcd.gcd(test_input_n, test_input_m) == expected

