class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from the queue
    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None


if __name__ == "__main__":
    q = Queue()
    while True:
        print("")
        print(" Queue OPERATION")
        print(" ------------------------------\n")
        print("\nSELECT APPROPRIATE CHOICE")
        print("1. Insert Element into queue")
        print("2. Delete element from queue")
        print("3. Display Elements in the queue")
        print("4. Exit")
        choice = int(input("Enter the Choice:"))
        if choice == 1:
            n = int(input("Enter the number of elements to insert into the queue: "))
            for i in range(0, n):
                element = int(input("Enter element: "))
                q.EnQueue(element)
        elif choice == 2:
            q.DeQueue()
            print("Front element Deleted")
        elif choice == 3:
            print("Queue Front: " + str(q.front.data if q.front is not None else -1))
            print("Queue Rear: " + str(q.rear.data if q.rear is not None else -1))
        elif choice == 4:
            break
