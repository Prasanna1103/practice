import reverse_int

def test_reverse():
    assert reverse_int.reverse(7234) == 4327
    assert reverse_int.reverse(1234) == 4321
    assert reverse_int.reverse(100) == 1
    assert reverse_int.reverse(0) == 0
    assert reverse_int.reverse(1) == 1
    assert reverse_int.reverse(10) == 1
