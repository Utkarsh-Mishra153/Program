# Creating the new node
class Node:   
    def __init__(self, info): 
        self.info = info
        self.left = None
        self.right = None
  
def lca(root, v1, v2):
    if root is None:
        return root
    if root.info == v1 or root.info == v2:
        return root
    if(v1>root.info and v2>root.info):
        return lca(root.right, v1, v2)
    if (v1<root.info and v2<root.info):
        return lca(root.left, v1, v2)
    return root

# Driver program to test above function 
root = Node(2)  
root.left = Node(1) 
root.right = Node(3) 
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)

n1 = 1 ; n2 = 3
t = lca(root, n1, n2) 
print(n1, n2, t.info)

n1 = 4 ; n2 = 5
t = lca(root, n1, n2) 
print(n1, n2, t.info)

n1 = 1 ; n2 = 5
t = lca(root, n1, n2) 
print(n1, n2, t.info)