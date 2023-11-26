# Tree Traversals
class N:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)

def postorder(root):
    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')

def preorder(root):
    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)

root = N(1)
root.left = N(2)
root.right = N(3)
root.left.left = N(4)
root.left.right = N(5)

print('')
print("Tree Traversals")
print("---------------\n")
print("Inorder traversal ")
inorder(root)
print('')
print("\nPreorder traversal ")
preorder(root)
print('')
print("\nPostorder traversal ")
postorder(root)
