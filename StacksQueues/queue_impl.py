class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.first.value
    
    def enqueue(self, val):
        new_node = Node(val)
        if self.first == None:
            self.first = new_node
            self.last = self.first
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        ptr = self.first.next
        rem_node = self.first
        if ptr == None:
            self.first = None
            self.length -= 1
            return 
        self.first.next =  None
        self.first = ptr
        self.length -= 1
    
    def print_queue(self):
        ptr = self.first
        while ptr != None:
            print(ptr.value, end = ' -> ')
            ptr = ptr.next
        print()

myq = Queue()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.print_queue()
myq.dequeue()
myq.print_queue()
x = myq.peek()
print(x)