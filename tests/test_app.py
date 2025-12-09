import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0,parent_dir)
from src.app import sub
def test_sub():
    assert sub(2, 3) == -1
