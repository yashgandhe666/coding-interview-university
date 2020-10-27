class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, val):
        if self.tail:
            temp = self.tail
            temp.next = Node(val)
            self.tail = temp.next
        else:
            self.tail = Node(val)
            self.head = self.tail
    
    def removeNode(self):
        if self.head:
            temp = self.head.val
            self.head = self.head.next
            return temp
        else:
            return "Error"
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
    
    

s = Queue()
s.addNode(5)
s.addNode(6)
s.addNode(7)
s.addNode(8)
s.printList()
s.removeNode()
s.removeNode()
s.printList()
