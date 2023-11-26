class Node:
    def __init__(self,data):
        self.item=data
        self.next=None
        self.prev=None
class doublyLinkedList:
    def __init__(self):
        self.start_node=None
    def InsertToEmptyList(self,data):
        if self.start_node is None:
            new_node=Node(data)
            self.start_node=new_node
        else:
            print("The list is empty")
    def InsertToEnd(self,data):
        if self.start_node is None:
            new_node=Node(data)
            self.start_node=new_node
            return
        n=self.start_node
        while n.next is not None:
            n=n.next
        new_node=Node(data)
        n.next=new_node
        new_node.prev=n
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The linked list is empty. No elements to delete")
            return
        if self.start_node.next is None:
            self.start_node=None
            return
        self.start_node=self.start_node.next
        self.start_prev=None
    def delete_at_end(self):
        if self.start_node is None:
            print("The linked list is Empty. No element to delete")
            return
        if self.start_node.next is None:
            self.start_node=None
            return
        n=self.start_node
        while n.next is not None:
            n=n.next
        n.prev.next=None
    def Display(self):
        if self.start_node is None:
            print("The list is Empty")
            return
        else:
            n=self.start_node
            while n is not None:
                print("Element is :",n.item)
                n=n.next
NewDoublyLinkedList=doublyLinkedList()
while True:
    print("")
    print("Doubly Linked List Operation")
    print("----------------------------")
    print("SELECT APPROPRIATE CHOICE")
    print("1. Insertion Operation")
    print("2. Display Elements of the list")
    print("3. Delete Elements at start")
    print("4. Delete Elements at end list")
    print("5. Exit")
    print("")
    choice=int(input("Enter the choice:"))
    if choice==1:
        input_string=int(input("Enter elements in the doubly linked list \n"))
        NewDoublyLinkedList.InsertToEnd(input_string)
        NewDoublyLinkedList.Display()
    elif choice==2:
        NewDoublyLinkedList.Display()
    elif choice==3:
        NewDoublyLinkedList.DeleteAtStart()
        NewDoublyLinkedList.Display()
    elif choice==4:
        NewDoublyLinkedList.delete_at_end()
        NewDoublyLinkedList.Display()
    elif choice==5:
        break
    else:
        print("Sorry!!! Wrong choice \n")
            
        