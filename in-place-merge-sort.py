import unittest
import random

def merge(array,left,mid,right):
    leftArrayIndex = left
    rightArrayIndex = mid + 1
    mergedArrayIndex = left
    while(leftArrayIndex <= mid and rightArrayIndex <= right):
        if(array[leftArrayIndex] <= array[rightArrayIndex]):
            array[mergedArrayIndex] = array[leftArrayIndex]
            leftArrayIndex += 1
        else:
            toBeAssigned = array[rightArrayIndex]
            for i in range(mid,leftArrayIndex-1,-1):
                temp = array[i]
                array[i+1] = temp
            array[mergedArrayIndex] = toBeAssigned    
            rightArrayIndex += 1
            mid +=1
            leftArrayIndex += 1
        mergedArrayIndex += 1
    
    while(leftArrayIndex<=mid):
        array[mergedArrayIndex] = array[leftArrayIndex]
        leftArrayIndex += 1
        mergedArrayIndex += 1

    while(rightArrayIndex<=right):
        array[mergedArrayIndex] = array[rightArrayIndex]
        rightArrayIndex += 1
        mergedArrayIndex += 1


def divide(array,begin,end):
    if(begin>=end):
        return
    mid = begin + (end-begin)//2
    divide(array,begin,mid)
    divide(array,mid + 1,end)
    merge(array,begin,mid,end)


class TestMergeSort(unittest.TestCase):
    def testMergeSortWithRandomArrays(self):
        testIteration = 100
        maxElement = 1000
        minElement = 0
        maxArrayLen = 20
        minArrayLen = 1
        for i in range(testIteration):
      
            testArray = []
            testArrayLen = random.randint(minArrayLen,maxArrayLen)
            for i in range(testArrayLen):
                newElement = random.randint(minElement,maxElement)
                testArray.append(newElement)
            testArrayCopy = [testArray[i] for i in range(testArrayLen)]
            print(testArray)
            testArrayCopy.sort()
            divide(testArray,0,testArrayLen-1)
            print(testArray)    
            self.assertListEqual(testArray,testArrayCopy)

if __name__ == "__main__":
    unittest.main()

