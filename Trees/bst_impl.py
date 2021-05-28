class Node:
  def __init__(self,val):
    self.value = val
    self.left = None
    self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = Node(val)

        if self.root == None:
            self.root = new_node 
            return
        else:
            curr_node = self.root
            while True:
                if val < curr_node.value:
                    if curr_node.left == None:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left
                elif val > curr_node.value:
                    if curr_node.right == None:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right

    def lookup(self, val):
        curr_node = self.root
        while True:
            if curr_node == None:
                return False
            if curr_node.value == val:
                return True
            elif val < curr_node.value:
                curr_node = curr_node.left
            elif val > curr_node.value:
                curr_node = curr_node.right

    def remove(self, value):
        if self.root == None: 
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node!=None: 
            if current_node.value > value:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                parent_node = current_node
                current_node = current_node.right
            else: 
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.value > current_node.value:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.value > current_node.value:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                elif current_node.left == None and current_node.right == None:
                    if parent_node == None: 
                        current_node = None
                        return
                    if parent_node.value > current_node.value:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None: 
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.value = del_node.value 
                    if del_node == del_node_parent: 
                        current_node.right = del_node.right
                        return
                    if del_node.right == None: 
                        del_node_parent.left = None
                        return
                    else: 
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"
 
    
    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
    
    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)

bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(13)
bst.insert(65)
bst.insert(0)
bst.insert(10)
'''
            5
        3       7
    1               13
0                10     65
'''

bst.remove(13)
'''
            5
        3       7
    1               65
0                10     
'''
bst.remove(5)
'''
            7
        3       65
    1        10     
0                
'''
bst.remove(3)
'''
            7
        1       65
    0        10                     
'''
bst.remove(7)
'''
            10
        1       65
    0                
'''
bst.remove(1)
'''
            10
        0       65
                     
'''
bst.remove(0)
'''
            10
                65
                     
'''
bst.remove(10)
'''
           65
                
                     
'''
bst.remove(65)
'''
           
                
'''

bst.insert(10)
'''
        10
'''
print(bst.root.value)
#10