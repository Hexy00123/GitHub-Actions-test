import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.main import add_correct, add_wrong


def test_add_correct():
    assert add_correct(1, 2) == 3
    assert add_correct(2, 1) == 3
    assert add_correct(-1, -2) == -3
    assert add_correct(0, 0) == 0


def test_add_wrong():
    assert add_wrong(1, 2) != 3
    assert add_wrong(2, 1) != 3
    assert add_wrong(-1, -2) != -3
    assert add_wrong(0, 0) != 0
