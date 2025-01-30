# Synchronous Execution:

# import time

# def task1():
#     print("Task 1 started")
#     time.sleep(3)  # Simulates a delay
#     print("Task 1 finished")

# def task2():
#     print("Task 2 started")
#     time.sleep(2)  # Simulates another delay
#     print("Task 2 finished")

# task1()
# task2()

# Output:
"""
Task 1 started
(Waits 3 seconds)
Task 1 finished
Task 2 started
(Waits 2 seconds)
Task 2 finished

"""

# Asynchronous Execution:
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)  # Simulates a delay
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)  # Simulates another delay
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())  # Run both tasks at the same time

asyncio.run(main())

# Output:
"""
Task 1 started
Task 2 started
(Waits 2 seconds)
Task 2 finished
(Waits 1 more second)
Task 1 finished
"""
