# Initial empty STACK
stack = []
stacksize = 5

# Display Menu with Choices
while True:
    print("")
    print("STACK ADT OPERATION")
    print("-----------------------------------\n")
    print("\nSELECT APPROPRIATE CHOICE")
    print("1. PUSH Element into the Stack")
    print("2. POP Element from the Stack")
    print("3. Display Elements of the Stack")
    print("4. Exit")
    print("")
    
    choice = int(input("Enter the Choice:"))
    
    # push
    if choice == 1:
        if len(stack) == stacksize:
            print("Stack is full")
        else:
            n = int(input("Enter the number of elements for the list:"))
            for i in range(0, n):
                element = input("Enter the element to push onto the stack:")
                stack.append(element)
            print('\nTotal elements PUSHED into the STACK', i + 1)
    
    # pop
    elif choice == 2:
        if len(stack) == 0:
            print('The STACK is EMPTY. No element to POP out')
        else:
            print('\nElement POPPED out from the STACK is:', stack.pop())
    
    # display the STACK
    elif choice == 3:
        if len(stack) == 0:
            print('The STACK is initially EMPTY')
        else:
            print("The Size of the STACK is: ", len(stack))
            print('\nSTACK elements are as follows:')
            print(stack)
    
    # EXIT from the program
    elif choice == 4:
        break
    
    # Shows ERROR message if the choice is not in between 1 to 4
    else:
        print("Incorrect Choice")
