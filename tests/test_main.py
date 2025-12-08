import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0,parent_dir)
from src.main import add
def test_add():
    assert add(2, 3) == 5
