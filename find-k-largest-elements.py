import unittest

def find_K_largest_elements(array,k):
    arrayLen = len(array)
    for j in range(k):
        for i in range(arrayLen-1-j):
            if(array[i]>array[i+1]):
                tempFirst = array[i]
                tempSecond = array[i+1]
                array[i] = tempSecond
                array[i+1] = tempFirst

    return array[arrayLen-k:arrayLen]

class TestFindKLargestElements(unittest.TestCase):
    def setUp(self) -> None:
        self.testArray = [8,7,6,5,4,3,2,9,1]
        self.numberOfLargestElementsToBeExtracted = 3
        self.expectedKLargestForTestArray = [7,8,9]

    def test_with_no_duplicate(self):
       result = find_K_largest_elements(self.testArray,self.numberOfLargestElementsToBeExtracted)
       self.assertListEqual(result,self.expectedKLargestForTestArray) 

if(__name__=="__main__"):
    unittest.main()


