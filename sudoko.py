testSudokoInput = [["5","3",".",".","7",".",".",".","."],
                   ["6",".",".","1","9","5",".",".","."],
                   [".","9","8",".",".",".",".","6","."],
                   ["8",".",".",".","6",".",".",".","3"],
                   ["4",".",".","8",".","3",".",".","1"],
                   ["7",".",".",".","2",".",".",".","6"],
                   [".","6",".",".",".",".","2","8","."],
                   [".",".",".","4","1","9",".",".","5"],
                   [".",".",".",".","8",".",".","7","9"]]

class Sudoko():

    def __init__(self,originalTwoDArray):
        self.originalTwoDArray = originalTwoDArray
        self.solvedTwoDArray = originalTwoDArray
        self.candidates = {}
        self.setInitialCandidate()
        self.firstSolutionReachedToEnd = False

    @staticmethod
    def formatBoardToStr(TwoDArray):
        result = ""
        for outerIndex,row in enumerate(TwoDArray):
            for index,element in enumerate(row):
                if element == ".":
                    result += "0"
                else:
                    result += element
                if (((index+1)%3)==0):
                    result += '|'    
            if (((outerIndex+1)%3)==0 and outerIndex != 8):
                result += '\n_________\n'
            elif(outerIndex != 8):
                result += '\n'       
        return result
    
    @staticmethod
    def getFlattenIndex(i,j):
        return i*9 + j

    @staticmethod    
    def reverseFlattenIndex(flattenIndex):
        i = flattenIndex//9
        j = flattenIndex%9
        return (i,j)
    
    def setInitialCandidate(self):
        for outerIndex, row in enumerate(self.originalTwoDArray):
            for innerIndex, element in enumerate(row):
                flattenIndex = Sudoko.getFlattenIndex(outerIndex,innerIndex)
                if element == ".":
                    self.candidates[flattenIndex] = [str(i+1) for i in range(9)]
                else:
                    self.candidates[flattenIndex] = [element]        
  
    def updateCandidate(self):
        for key,values in self.candidates.items():
            rejecteds = self.getElementsThatArePresentInAnyOfTheThreePossibleScenario(key)
            tempCandidatesForCurrentElements =  [element for element in self.candidates[key]]
            for e in self.candidates[key]:
                if e in rejecteds:
                    tempCandidatesForCurrentElements.remove(e)
            self.candidates[key] = tempCandidatesForCurrentElements  

    def getElementsThatArePresentInAnyOfTheThreePossibleScenario(self,index):    
        return set(Sudoko.getBoxElements(self,index) + Sudoko.getColumnElements(self,index) + Sudoko.getRowElements(self,index))

    def getBoxElements(self,index):
        originalI,originalJ = Sudoko.reverseFlattenIndex(index)
        iMin = originalI - originalI%3
        iMax = iMin + 3 
        jMin = originalJ - originalJ%3
        jMax = jMin + 3
        result = []
        for i in range(iMin,iMax):
            for j in range(jMin,jMax):
                if not (i==originalI and j==originalJ):
                    if not self.solvedTwoDArray[i][j] == '.':
                        result.append(self.solvedTwoDArray[i][j])
        return result
    
    def replaceIfFoundAnyThing(self):
        foundNothing = True
        for key,values in self.candidates.items():
            i,j = Sudoko.reverseFlattenIndex(key)
            if len(values) == 1 and self.solvedTwoDArray[i][j] == '.':
                foundNothing = False
                self.solvedTwoDArray[i][j] = values[0]
        if foundNothing:
            self.firstSolutionReachedToEnd = True

    def getRowElements(self,index):
        originalI,originalJ = Sudoko.reverseFlattenIndex(index)
        results = []
        for j in range(9):
            if j != originalJ and self.solvedTwoDArray[originalI][j] != '.':
                results.append(self.solvedTwoDArray[originalI][j])
        return results        

    def getColumnElements(self,index):
        originalI,originalJ = Sudoko.reverseFlattenIndex(index)
        results = []
        for i in range(9):
            if i != originalI and self.solvedTwoDArray[i][originalJ] != '.':
                results.append(self.solvedTwoDArray[i][originalJ])
        return results

    def solveWithoutImprovise(self):
        while not self.firstSolutionReachedToEnd:            
            self.updateCandidate()
            self.replaceIfFoundAnyThing()

    def __str__(self):
        return Sudoko.formatBoardToStr(self.originalTwoDArray) + "\n=========\n" + Sudoko.formatBoardToStr(self.solvedTwoDArray) + "\n=========\n" 

if __name__ == "__main__":
    testSudoko = Sudoko(testSudokoInput)
    print(testSudoko)
    testSudoko.solveWithoutImprovise()
    print(testSudoko)
