
import unittest

def findNumber(array, start, end, value): 
    #Write your code here
    if end >= start:
        mid = (start+end)//2
        if array[start] == value:
            return start
        elif array[mid] == value:
            return mid
        elif array[mid] > value and array[start] > value:
            start = mid + 1
            return findNumber(array, start, end, value)
        elif array[mid] > value and array[start] < value:
            end = mid - 1
            return findNumber(array, start, end, value)
        elif array[mid] < value and array[start] < value:
            start = mid + 1
            return findNumber(array, start, end, value)
        elif array[mid] < value and array[start] > value:
            start = mid + 1
            return findNumber(array, start, end, value)
    else:    
        return -1 
  #ok for all test cases required  
class Test(unittest.TestCase):

    def test_findNumber1(self):
        actual = findNumber([3, 4, 5, 6, 7, 8, 9, 10, 1, 2],0,9,1)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber2(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3],0,8,3)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber3(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3],0,8,28)
        expected = -1
        self.assertEqual(actual, expected)
    
    def test_findNumber4(self):
        actual = findNumber([30, 40, 50, 10, 20],0,4,10)
        expected = 3
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)     
    
