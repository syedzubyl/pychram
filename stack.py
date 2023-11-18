stack = []
stackSize = 5
while True:
    print("The STACK ADT OPERATION")
    print("----------------------- \n")
    print("\n SELECT APPROPRIATE CHOICE")
    print("1. PUSH Element into the stack")
    print("2. pop the element into the stack")
    print("3. Display the element in the stack")
    print("4.Exit")
    print(" ")
    choice = int(input("Enter the Choice:"))
    if choice == 1:
        if len(stack) == stackSize:
            print("Stack is full")
        else:
            n = int(input("Enter the len into stack"))
            for i in range(0,n):
                ele=int(input("enter the element to push on to stack"))