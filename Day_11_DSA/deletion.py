#deletion operation
class Node:
    def __init__(self,key) -> None:
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
def insert(root,key):
    if root is None:
        return Node(key)
    elif key>root.value:
        root.right=insert(root.right,key)
    else:
        root.left=insert(root.left,key)
    return root
def minValueNode(node):
    current = node
 
    while(current.left is not None):
        current = current.left
 
    return current
def delete(root,key):
    if root is None:
        return root
    if key<root.value:
        root.left=delete(root.left,key)
    elif key>root.value:
        root.right=delete(root.right,key)
    else:
        if root.left==None:
            temp=root.right
            root=None
            return temp
        elif root.right==None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.value = temp.value

        root.right = delete(root.right, temp.value)
 
    return root
        
                   
root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
root.inorder(root)
print()
root.preorder(root)
print()
root=delete(root,10)
root.postorder(root)
root=delete(root,4)
root.inorder(root)
root.postorder(root)