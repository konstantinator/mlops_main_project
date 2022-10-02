


import pytest
import os.path
import sys

# go up one directory level from this file's directory:
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# prepend parent directory to the system path:
sys.path.insert(0, path)


from src.training import ab

def test_2_add_2():
    print("test")

@pytest.mark.parametrize('a, b, exp_result', [(1,2,3),
                                            (2,3,5),
                                            (4,2,6),
                                            (7,3,10)])
def test_sum(a, b, exp_result):
    assert ab(a, b)==exp_result