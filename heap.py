import heapq as hq
import time

# Jobs and Interrupts
jobs = [(2, 'task_1'), (5, 'task_2'), (1, 'task_4'), (4, 'task_5'), (3, 'task_3'), (1, 'task_8')]
interrupts = [(1, 'intr_1'), (2, 'intr_2'), (13, 'intr_3')]

# Initializing indices
i, j = 0, 0

# Arranging jobs in heap
hq.heapify(jobs)

print(jobs, "\n\n")

# Scheduling the tasks
while len(jobs) != 0:

    # Printing execution log
    print("The ", jobs[0][1], " with priority ", jobs[0][0], " in progress", end="")

    # Servicing the tasks
    for _ in range(0, 5):
        print(".", end="")
        time.sleep(0.5)

    # Pop the job that completed
    hq.heappop(jobs)

    # Adding interrupts
    if j < len(interrupts):
        hq.heappush(jobs, interrupts[j])
        print("\n\nNew interrupt arrived!!", interrupts[j])
        print()
        j = j + 1

    # Job queue after arrival of interrupt
    print("\n Job queue currently :", jobs)
    print("\n")

print("\nAll interrupts and jobs completed!")
