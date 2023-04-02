class Node:
    def __init__(self,key) :
        self.left=None
        self.right=None
        self.value=key
    def inorder(s,root):
        if root:
            s.inorder(root.left)
            print(str(root.value) + "->",end=" ")
            s.inorder(root.right)
    def preorder(s,root):
        if root:
            print(str(root.value) + "->",end=" ")
            s.preorder(root.left)
            s.preorder(root.right)
    def postorder(s,root):
        if root:
            s.postorder(root.left)
            s.postorder(root.right)
            print(str(root.value) + "->",end=" ")
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
root.left.left=Node(5)
root.right.right=Node(6)
root.right.left=Node(7)

root.preorder(root)
print()
root.inorder(root)
print()
root.postorder(root)



    
    
    
    
        
        