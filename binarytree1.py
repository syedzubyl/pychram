class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
def minValueNode(node):
    current = node
    while (current.left is not None):
        current = current.left
    return current
def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif (key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root
def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("\n")
while (True):
    print("\n")
    print("Binary search Tree\n")
    print("------------------\n")
    print("1. Insertion Operation\n")
    print("2. Deletion Operation\n")
    print("3. Search Operation\n")
    print("4. Inorder Traversal\n")
    print("5. exit\n")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        print("Insertion into the following Binary Search Tree")
        print("***********************************************")
        print("\n")
        inorder(root)
        nne = int(input("\nEnter the non duplicate element \n"))
        insert(root, nne)
        print("\n")
        print("Inserted Binary Search Tree")
        inorder(root)
    elif choice == 2:
        print("Deletion")
        print("********")
        element = int(input("Enter the element to delete"))
        print("\nDeleted Element", element)
        root = deleteNode(root, element)
        print("Inorder traversal: ", end=' ')
        inorder(root)
    elif choice == 3:
        print("Searching\n")
        print("**********")
        x = int(input("Enter the element to search "))
        key = x
        if search(root, key) is None:
            print("The searched Element", key, "is not found")
        else:
            print("The searched Element", key, "is found")
    elif choice == 4:
        print("Inorder traversal:\n ", end=' ')
        inorder(root)
        print("\n")
    elif choice == 5:
        break
    else:
        print("Sorry!!!Wrong choice.\n")
