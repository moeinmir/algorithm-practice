LIST_MAX_LEN = 5

class Node:
    def __init__(self,data):
        self.maxLen = LIST_MAX_LEN
        self.currentLen = 1
        self.data = data
        self.next = self
        self.prev = self
        self.current = self
        self.start = self
     
    def insert(self,data):        
        newNode = Node(data)
        if(self.currentLen<self.maxLen):
            self.currentLen += 1    
            self.current.next = newNode
            newNode.prev = self.current
            newNode.next = self.start
            self.start.prev = newNode
            self.current = newNode
        else:
            newStart = self.start.next
            newNode.next = self.start.next
            newNode.prev = self.start.prev
            self.start.prev.next = newNode
            self.start.next.prev = newNode
            self.start = newStart
   
    
    def traverse(self):
        traversingNode = self.start
        while(traversingNode):
            print(traversingNode.data)
            traversingNode = traversingNode.next
            if(traversingNode==self.start):
                break

if (__name__=="__main__"):
    testNode = Node(4)
    for i in range(5,21):
        testNode.insert(i)
        print("################################")
        testNode.traverse()
