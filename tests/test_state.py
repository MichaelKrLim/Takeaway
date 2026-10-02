from lib.State import *

def test_toggle_item():
    s=State(set(),None)
    s.toggle_item("asdf")
    s.toggle_item("fdsa")
    s.toggle_item("asdf")
    assert s.basket=={"fdsa"}
