class Node: 
  
    # function to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None
  
  
# Print level order traversal of tree 
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
  
# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(f"{root.data}-> ", end="")
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 
  
  
#Compute the height of a tree the number of nodes along the longest path from the root node down to the farthest leaf node
def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 

        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

# Driver program to test above function 
root = Node(1)  
root.right = Node(2) 
root.right.right = Node(5) 
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)

printLevelOrder(root) 