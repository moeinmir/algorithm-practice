"""
calculate the median of merged array of two sorted array with complexity of O(log(m+n))
"""

## 40 percent of the tests fails and needs debugging
## in case of time complexity it follows a correct logic

import unittest
import random
import logging 
logger = logging.getLogger(__file__)

def getPossibleIndexesOfElementInMergedArray(otherSortedArray,element,index):
    step = len(otherSortedArray)
    indexInOtherSortedArray = step//2
    lastIndex = len(otherSortedArray)-1
    if otherSortedArray[0] > element:
            return [index]
    if otherSortedArray[lastIndex] < element:
        return [lastIndex+index]
    while True:
        if otherSortedArray[indexInOtherSortedArray] == element:
            return [index+indexInOtherSortedArray,index+indexInOtherSortedArray+1]
        elif(step==1 and otherSortedArray[indexInOtherSortedArray]<element):
            return [index+indexInOtherSortedArray+1]
        elif(step==1 and otherSortedArray[indexInOtherSortedArray]>element):
            step = 2
        elif(step>1 and otherSortedArray[indexInOtherSortedArray]<element):
            step = step//2
            if step == 0:
                step = 1
            indexInOtherSortedArray = indexInOtherSortedArray + step
            if(indexInOtherSortedArray>lastIndex):
                indexInOtherSortedArray = lastIndex
        else:
            step = step//2
            if(step==0):
                step = 1
            indexInOtherSortedArray = indexInOtherSortedArray -step
            if(indexInOtherSortedArray<0):
                indexInOtherSortedArray = 0

def getMedianIndexes(firstArray,secondArray):
    firstArrayLength = len(firstArray)
    secondArrayLength = len(secondArray)
    mergedArrayLength = firstArrayLength + secondArrayLength
    if mergedArrayLength%2==1:
        medianIndexes = [mergedArrayLength//2]
    else:
        medianIndexes = mergedArrayLength//2    
        medianIndexes = [medianIndexes-1,medianIndexes]
    return medianIndexes

def whatDirectionToMove(otherArray,element,index,medianIndex):
    possibleIndexesInMergedArray = getPossibleIndexesOfElementInMergedArray(otherArray,element,index)
    if medianIndex in possibleIndexesInMergedArray:
        return 0
    for possibleIndexInMergedArray in possibleIndexesInMergedArray:
        if(possibleIndexInMergedArray<medianIndex):
            return 1
        else:
            return -1

def getMedianElementIndexIfItExistInThisArray(possibleArrayToContainMedian,otherSortedArray,medianIndex):
    step = len(possibleArrayToContainMedian)
    indexInPossibleArrayToContainMedian = step//2
    lastIndex = len(possibleArrayToContainMedian)-1
    while True:
        directionToMove = whatDirectionToMove(otherSortedArray,possibleArrayToContainMedian[indexInPossibleArrayToContainMedian],indexInPossibleArrayToContainMedian,medianIndex)
        if(directionToMove==0):
            return indexInPossibleArrayToContainMedian
        elif(step>1 and directionToMove==-1):
            step = step//2
            if(step==0):
                step =1
            indexInPossibleArrayToContainMedian = indexInPossibleArrayToContainMedian - step
            if(indexInPossibleArrayToContainMedian < 0):
                indexInPossibleArrayToContainMedian = 0                
        elif(step>1 and directionToMove==1):
            step = step//2
            if(step==0):
                step =1
            indexInPossibleArrayToContainMedian = indexInPossibleArrayToContainMedian + step
            if(indexInPossibleArrayToContainMedian>lastIndex):
                indexInPossibleArrayToContainMedian = lastIndex
        else:
            if whatDirectionToMove(otherSortedArray,possibleArrayToContainMedian[indexInPossibleArrayToContainMedian],indexInPossibleArrayToContainMedian,medianIndex)==0:
                return indexInPossibleArrayToContainMedian
            return -1

def getMedianOfTwoSortedArray(arrayOne,arrayTwo):
    medianIndexes = getMedianIndexes(arrayOne,arrayTwo)
    result = []
    for medianIndex in medianIndexes:
        possibleMedianIndexInArrayOne = getMedianElementIndexIfItExistInThisArray(arrayOne,arrayTwo,medianIndex)
        if(possibleMedianIndexInArrayOne>=0):
            result.append(arrayOne[possibleMedianIndexInArrayOne])
        else:
            medianIndexInArrayTwo = getMedianElementIndexIfItExistInThisArray(arrayTwo,arrayOne,medianIndex)
            result.append(arrayTwo[medianIndexInArrayTwo])      
    return sum(result)/len(result)

# required for testing
def mergeTwoSortedArray(arrayOne,arrayTwo):
    movingIndexInArrayOne = 0
    movingIndexInArrayTwo = 0
    movingIndexInMergedArray = 0
    arrayOneLen = len(arrayOne)
    arrayTwoLen = len(arrayTwo)
    mergedArrayLen = arrayOneLen+ arrayTwoLen
    mergedArray = [0 for i in range(mergedArrayLen)]
    while True:
        if(movingIndexInMergedArray==mergedArrayLen):
            break   
        elif(movingIndexInArrayOne==arrayOneLen):
            mergedArray[movingIndexInMergedArray] = arrayTwo[movingIndexInArrayTwo]
            movingIndexInArrayTwo += 1
        elif(movingIndexInArrayTwo==arrayTwoLen):
            mergedArray[movingIndexInMergedArray] = arrayOne[movingIndexInArrayOne]
            movingIndexInArrayOne += 1
        elif(arrayOne[movingIndexInArrayOne]<=arrayTwo[movingIndexInArrayTwo]):
            mergedArray[movingIndexInMergedArray] = arrayOne[movingIndexInArrayOne]
            movingIndexInArrayOne += 1
        else:
            mergedArray[movingIndexInMergedArray] = arrayTwo[movingIndexInArrayTwo] 
            movingIndexInArrayTwo += 1   
        movingIndexInMergedArray += 1
    return mergedArray

# required for testing
def getTheMedianOfASortedArray(sortedArray):
    sortedArrayLen = len(sortedArray)
    halfOfSortedArrayLen = sortedArrayLen//2
    result = []
    result.append(sortedArray[halfOfSortedArrayLen])
    if(sortedArrayLen%2==0):
        result.append(sortedArray[halfOfSortedArrayLen-1])
    return sum(result)/len(result)

class TestFindingTheMidianOfToSortedArray(unittest.TestCase):
    def setUp(self) -> None:
        self.firstTestArray = [1,2,4,56,56,89,100] 
        self.secondTestArray = [57,93,102,104]
        self.thirdTestArray = [57,89,93,102,104]
    def testGetMedianIndexes(self):
        oddCaseResult = getMedianIndexes(self.firstTestArray,self.secondTestArray)
        oddCaseExpectedResult = [5]
        self.assertListEqual(oddCaseResult,oddCaseExpectedResult)
        evenCaseResult = getMedianIndexes(self.firstTestArray,self.thirdTestArray)
        evenCaseExpectedResult = [5,6]
        self.assertListEqual(evenCaseResult,evenCaseExpectedResult)

    def testGetPossibleIndexesOfElementInMergedArray(self):
        oddCaseResult = getPossibleIndexesOfElementInMergedArray(self.secondTestArray,89,5)
        oddCaseExpectedResult = [6]
        self.assertListEqual(oddCaseResult,oddCaseExpectedResult)
        evenCaseResult = getPossibleIndexesOfElementInMergedArray(self.thirdTestArray,89,5)
        evenCaseExpectedResult = [6,7]
        self.assertListEqual(evenCaseResult,evenCaseExpectedResult)


    def testWhatDirectionToMove(self):
        result = whatDirectionToMove(self.secondTestArray,56,4,5)
        expectedResult = 1
        self.assertEqual(result,expectedResult)
        
    def testGetMedianOfTwoSortedArray(self):
        result = getMedianOfTwoSortedArray(self.firstTestArray,self.secondTestArray)
        sortedArray = mergeTwoSortedArray(self.firstTestArray,self.secondTestArray)
        expectedResult = getTheMedianOfASortedArray(sortedArray)
        self.assertEqual(result,expectedResult)
        
        result = getMedianOfTwoSortedArray(self.firstTestArray,self.thirdTestArray)
        sortedArray = mergeTwoSortedArray(self.firstTestArray,self.thirdTestArray)
        expectedResult = getTheMedianOfASortedArray(sortedArray)
        self.assertEqual(result,expectedResult)


    def testGetMedianOfTwoSortedArrayWithRandomInput(self):
        maxNumber = 100
        minNumber = 1
        maxArrayLen = 10
        minArrayLen = 2
        testIteration = 100
        numberOfFailures = 0 
        for i in range(testIteration):
            firstArray = []
            secondArray = []
            firstArrayLen = random.randint(minArrayLen,maxArrayLen)
            secondArrayLen = random.randint(minArrayLen,maxArrayLen)
            for i in range(firstArrayLen):firstArray.append(random.randint(minNumber,maxNumber))
            for i in range(secondArrayLen):secondArray.append(random.randint(minNumber,maxNumber))
            firstArray.sort()
            secondArray.sort()
            result = getMedianOfTwoSortedArray(firstArray,secondArray)
            sortedArray = mergeTwoSortedArray(firstArray,secondArray)
            expectedResult = getTheMedianOfASortedArray(sortedArray)
            try:
                self.assertEqual(result,expectedResult) 
            except:
                logger.error(f"first array: {firstArray}")
                logger.error(f"second array: {secondArray}")
                numberOfFailures += 1
                logger.error(f"number of failures: {numberOfFailures}")
if __name__ == "__main__":
    unittest.main()