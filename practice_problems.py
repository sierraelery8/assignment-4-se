"""
Problem 1: Duplicate Tracker 
 
You are given a collection of product IDs. Some IDs may appear more than once. 
Write a function that returns True if any duplicates are found, and False otherwise. 
 
Example: 
Input: [10, 20, 30, 20, 40] 
Output: True 
 
Input: [1, 2, 3, 4, 5] 
Output: False 
"""


def has_duplicates(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True

        seen.add(product_id)

    return False


# Justification:
# I chose a set because this problem requires checking whether a product ID has
# already appeared. Sets are designed for fast membership checks, making this
# solution efficient with an expected runtime of O(n) because we check each ID once.


"""
Problem 2: Order Manager 
 
You need to maintain a list of tasks in the order they were added, and support removing tasks from the front. 
Implement a class that supports add_task(task) and remove_oldest_task(). 
 
Example: 
task_queue = TaskQueue() 
task_queue.add_task("Email follow-up") 
task_queue.add_task("Code review") 
task_queue.remove_oldest_task() → "Email follow-up"
"""


class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if len(self.tasks) > 0:
            return self.tasks.pop(0)

        return None


# Justification:
# I chose a queue structure because tasks need to be processed in the order they
# were added (First In, First Out). Adding a task is O(1), but removing from the
# front of a list is O(n) because remaining items must shift positions.


"""
Problem 3: Unique Value Counter 
 
You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far. 
 
Example: 
tracker = UniqueTracker() 
tracker.add(10) 
tracker.add(20) 
tracker.add(10) 
tracker.get_unique_count() → 2
"""


class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


# Justification:
# I chose a set because it automatically prevents duplicate values and allows
# quick membership tracking. Adding values has an expected runtime of O(1), and
# returning the count is O(1) because the set stores its size.