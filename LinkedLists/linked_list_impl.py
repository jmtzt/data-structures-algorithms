class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):

        if index >= self.length:
            self.append(data)
            return 
        if index == 0:
            self.prepend(data)
            return 

        new_node = Node(data)

        leader = self.traverse_to_index(index - 1)
        ptr = leader.next
        leader.next = new_node 
        new_node.next = ptr
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return 

        if index > self.length:
            print("Invalid index")
            return

        leader = self.traverse_to_index(index - 1)
        del_node = leader.next
        leader.next = del_node.next
        self.length -= 1
        
    def traverse_to_index(self, index):
        i = 0
        cur_node = self.head
        while i != index:
            cur_node = cur_node.next
            i += 1
        return cur_node

    def printl(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data , end = ' ')
            tmp = tmp.next

    def reverse(self):
        prev = None 
        curr = self.head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(2,99)
l.insert(34,23)
l.remove(0)
l.printl()
l.reverse()
print()
l.printl()