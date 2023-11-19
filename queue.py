# QUEUE ADT
# initializing empty myQueue

myQueue = list()
queueSize = 10


def isEmpty(myQueue):
    if len(myQueue) == 0:
        return True
    else:
        return False


def dequeue(myQueue):
    if not (isEmpty(myQueue)):
        return myQueue.pop(0)
    else:
        return "Queue is empty so no items to remove"


def size(myQueue):
    return len(myQueue)


while (True):
    print("               QUEUE OPERATION")
    print("               ---------------")
    print("1. Enqueue Operation\n")
    print("2. Dequeue Operation\n")
    print("3. Size of  Queue\n")
    print("4. Display Queue\n")
    print("5. exit\n")
    choice = int(input("Enter your choice :"))
    # if user enters 1 then do this
    if choice == 1:
        n = int(input("Enter the number of elements for enqueue operation:"))
        for i in range(0, n):
            element = input("Enter the number to add items to the queue:")
            myQueue.append(element)
        print("Number of Items added to the Queue:", n)
        continue
    elif choice == 2:
        qitem = dequeue(myQueue)
        print("The Item removed is : ", qitem)
        continue
    elif choice == 3:
        print("The number of Items in the Queue = ", size(myQueue))
        continue
    elif choice == 4:
        print(myQueue)
    elif choice == 5:
        break
    else:
        print("Sorry!!!Wrong choice.\n")
