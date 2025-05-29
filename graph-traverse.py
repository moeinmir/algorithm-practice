
from abc import abstractmethod
import unittest

def addEdge(adjacentArray,sourceNode,targetNode):
    adjacentArray[sourceNode].append(targetNode)

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class Container:
    def __init__(self,data) -> None:
        self.start = Node(data)
        self.end = Node(data)
        pass

    def add(self,data):
        newNode = Node(data)
        if(self.end):
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode
        else:
            self.end = newNode 
        if(not self.start):
            self.start = newNode    

    @abstractmethod    
    def remove(self):
        pass        

class Stack(Container):
    def remove(self):
        toBeReturned = self.end
        if(self.end):
            self.end = self.end.prev
            if(self.end):
                self.end.next = None
            return toBeReturned
        else:
            return toBeReturned
        
class Queue(Container):
    def remove(self):
        toBeReturned = self.start
        if(self.start):
            if(self.start.next):
                self.start = self.start.next
                self.start.prev = None
                return toBeReturned
            else:
                self.start = None    
                return toBeReturned
        else:
            return toBeReturned

def traverse(graph,containerContainingStartVertice):
    graphTraverseOrder = []
    numberOfVertices = len(graph)
    verticeVisitStatus = [False]*numberOfVertices
    verticeVisitOrderHandler = containerContainingStartVertice
    while True:
        currentNode = verticeVisitOrderHandler.remove()
        if(not currentNode): break
        graphTraverseOrder.append(currentNode.data)
        verticeVisitStatus[currentNode.data] = True
        for vertice in graph[currentNode.data]:
            while(not verticeVisitStatus[vertice]):
                verticeVisitOrderHandler.add(vertice)
                verticeVisitStatus[vertice] = True
    return graphTraverseOrder

class TestTraverse(unittest.TestCase):
    def setUp(self) -> None:
            self.testGraphNumberOfVertices = 8
            self.testAdjacentArray = [[] for _ in range(self.testGraphNumberOfVertices)]
            self.testAdjacentArray[0].append(1)
            self.testAdjacentArray[0].append(2)    
            self.testAdjacentArray[1].append(3)    
            self.testAdjacentArray[1].append(4)    
            self.testAdjacentArray[2].append(5)    
            self.testAdjacentArray[3].append(6)    
            self.testAdjacentArray[3].append(7)
            self.breadthFirstSearchCorrectTraverseOrder = [0,1,2,3,4,5,6,7]
            self.deepFirsSearchCorrectTraverseOrder = [0,2,5,1,4,3,7,6]

    def test_breadth_first_search_traverse(self):
        queue = Queue(0)    
        breadthFirstSearchTraverseResult = traverse(self.testAdjacentArray,queue)
        for i in range(self.testGraphNumberOfVertices):
            self.assertEqual(breadthFirstSearchTraverseResult[i],self.breadthFirstSearchCorrectTraverseOrder[i])
    def test_deep_first_search_traverse(self):
        stack = Stack(0)
        deepFirstSearchTraverseResult = traverse(self.testAdjacentArray,stack)
        for i in range(self.testGraphNumberOfVertices):
            self.assertEqual(deepFirstSearchTraverseResult[i],self.deepFirsSearchCorrectTraverseOrder[i])

if(__name__=="__main__"):
    unittest.main()


