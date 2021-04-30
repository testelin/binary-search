from binarySearch import *

def test_findtwo():
    arr = [ 2, 3, 4, 10, 40 ]
    x = 2
    result = bs(arr, 0, len(arr)-1, x)
    assert result  == 0

def test_findfive():
    arr = [ 2, 3, 4, 10, 40 ]
    x = 5
    result = bs(arr, 0, len(arr)-1, x)
    assert result == -1
