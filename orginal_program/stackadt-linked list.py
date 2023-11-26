class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            print("Stack empty")
        else:
            # Removes the head node and makes
            # the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None

        else:
            return self.head.data

    # Prints out the stack
    def display(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:

            while iternode is not None:

                print(iternode.data, end="")
                iternode = iternode.next
                if iternode is not None:
                    print(" -> ", end="")
            return


# Driver code
if __name__ == "__main__":
    Mystack = Stack()
    while True:
        print("")
        print(" Stack OPERATION")
        print(" ------------------------------\n")
        print("\nSELECT APPROPRIATE CHOICE")
        print("1. Insert Element into Stack")
        print("2. Delete element from stack ")
        print("3. Display Elements in the stack")
        print("4. Exit")
        choice = int(input("Enter the Choice:"))
        if choice == 1:
            n = (int(input("Enter Elements to stack \n")))
            for i in range(0, n):
                element = int(input("Enter the number to add items to the stack"))
                Mystack.push(element)
        elif choice == 2:
            Mystack.pop()
            print("The topmost node deleted")
        elif choice == 3:
            Mystack.display()
            Mystack.peek()
        elif choice == 4:
            break
