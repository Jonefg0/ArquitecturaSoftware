
import min
def test_min():
    values = [1,5,10,2]
    assert min.get_min(values)== 1

def test_min2():
    values = [4,3,56,43]
    assert min.get_min(values) == 3