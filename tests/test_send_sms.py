from lib.send_sms import *

def test_to_international() -> str:
    assert to_international("03828183843")=="443828183843"
    assert to_international("0032342344")=="32342344"
