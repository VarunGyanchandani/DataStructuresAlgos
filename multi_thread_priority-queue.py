import threading
import queue
import time

def worker(pq, thread_id):
    while True:
        try:
            # Get a task from the priority queue
            priority, task = pq.get(timeout=3)  # Wait for a task for 3 seconds
            print(f"Thread {thread_id} processing task: {task} with priority {priority}")
            time.sleep(1)  # Simulate processing time
            pq.task_done()
        except queue.Empty:
            print(f"Thread {thread_id} found no tasks and is exiting.")
            break

# Create a PriorityQueue instance
pq = queue.PriorityQueue()

# Add some tasks with different priorities
tasks = [
    (3, "Task 1"),  # Priority 3
    (1, "Task 2"),  # Priority 1 (highest priority)
    (4, "Task 3"),  # Priority 4
    (2, "Task 4"),  # Priority 2
]

for task in tasks:
    pq.put(task)

# Create multiple threads
num_threads = 3
threads = []

for i in range(num_threads):
    thread = threading.Thread(target=worker, args=(pq, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All tasks have been processed.")
