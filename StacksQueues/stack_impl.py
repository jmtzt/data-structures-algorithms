class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        return self.top.value

    def push(self, val):
        new_node = Node(val)
        if self.bottom == None:
            self.bottom = new_node
            self.top = self.bottom
            self.length = 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1

    def pop(self):
        if not self.top:
            return None
        ptr = self.top
        self.top = self.top.next
        self.length -= 1
        if self.length == 0:
            self.bottom = None
        return ptr.value
    
    def print_stack(self):
        ptr = self.top
        while ptr != None:
            print(ptr.value, end = ' -> ')
            ptr = ptr.next
        print()
        
mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
mystack.print_stack()
print('\npeeking top of stack')
print(mystack.peek())
print()
print('pop stack')
y=mystack.pop()
print(y + "\n")
mystack.print_stack()