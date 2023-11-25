# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:52:55 2023

@author: Vimala Priya
"""

#DOUBLY LINKED LIST 

class Node: 

    def __init__(self, data): 

        self.item = data 

        self.next = None 

        self.prev = None 

# Class for doubly Linked List 

class doublyLinkedList: 

    def __init__(self): 

        self.start_node = None 

    # Insert Element to Empty list 

    def InsertToEmptyList(self, data): 

        if self.start_node is None: 

            new_node = Node(data) 

            self.start_node = new_node 

        else: 

            print("The list is empty") 

    # Insert element at the end 

    def InsertToEnd(self, data): 

        # Check if the list is empty 

        if self.start_node is None: 

            new_node = Node(data) 

            self.start_node = new_node 

            return 

        n = self.start_node 

        # Iterate till the next reaches NULL 

        while n.next is not None: 

            n = n.next 

        new_node = Node(data) 

        n.next = new_node 

        new_node.prev = n 

    # Delete the elements from the start 

    def DeleteAtStart(self): 

        if self.start_node is None: 

            print("The Linked list is empty, no element to delete") 

            return  

        if self.start_node.next is None: 

            self.start_node = None 

            return 

        self.start_node = self.start_node.next 

        self.start_prev = None; 

    # Delete the elements from the end 

    def delete_at_end(self): 

        # Check if the List is empty 

        if self.start_node is None: 

            print("The Linked list is empty, no element to delete") 

            return  

        if self.start_node.next is None: 

            self.start_node = None 

            return 

        n = self.start_node 

        while n.next is not None: 

            n = n.next 

        n.prev.next = None 

    # Traversing and Displaying each element of the list 

    def Display(self): 

        if self.start_node is None: 

            print("The list is empty") 

            return 

        else: 

            n = self.start_node 

            while n is not None: 

                print("Element is: ", n.item) 

                n = n.next 

       

# Create a new Doubly Linked List 

NewDoublyLinkedList = doublyLinkedList() 

while True: 

    print("") 

    print(" Doubly Linked List Operation") 

    print(" ------------------------------\n") 

    print("SELECT APPROPRIATE CHOICE")  

    print("1. Insertion Operation")  

    print("2. Display Elements of the List")  

    print("3. Delete  Elements at start")  

    print("4. Delete  Elements at end List")  

    print("5. Exit" )  

    print("") 

    choice = int(input("Enter the Choice:"))  

    #if choice == 1: 

        #NewDoublyLinkedList = doublyLinkedList() 

        #input_string = int(input("Enter an Element to the Empty Doubly Linked List \n")) 

       # NewDoublyLinkedList.InsertToEmptyList(input_string) 

        #NewDoublyLinkedList.Display()  

    if choice == 1: 

        input_string = int(input("Enter Elements in the doubly linked list \n")) 

        NewDoublyLinkedList.InsertToEnd(input_string) 

        NewDoublyLinkedList.Display() 

    elif choice == 2: 

        NewDoublyLinkedList.Display() 

    elif choice == 3: 

        NewDoublyLinkedList.DeleteAtStart() 

        NewDoublyLinkedList.Display() 

    elif choice == 4: 

        NewDoublyLinkedList.delete_at_end() 

        NewDoublyLinkedList.Display() 

    elif choice == 5: 

        break 

    else: 

        print("Sorry!!!Wrong choice.\n") 

 