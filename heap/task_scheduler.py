# Task Scheduler
# Medium
# Topics
# Company Tags
# Hints
# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

# Return the minimum number of CPU cycles required to complete all tasks.

# Example 1:

# Input: tasks = ["X","X","Y","Y"], n = 2

# Output: 5
# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

# Example 2:

# Input: tasks = ["A","A","A","B","C"], n = 3

# Output: 9
# Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

# Constraints:

# 1 <= tasks.length <= 1000
# 0 <= n <= 100

import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        my_dict = {}
        res = []

        for task in tasks:
            if task in my_dict:
                my_dict[task] += 1
            else:
                my_dict[task] = 1

        max_heap = [[-count, task] for task, count in my_dict.items()]

        # 2. Heap бүтэц рүү шилжүүлэх
        heapq.heapify(max_heap)


        # for heap in max_heap:
        idx = 0

        print("first heap ",max_heap)

        while max_heap:
            
            res.append(max_heap[idx][1])

            max_heap[idx][0] = max_heap[idx][0] + 1

            if max_heap[idx][0] == 0:
                print("before pop", max_heap)
                heapq.heappop(max_heap)
                print("after pop", max_heap)


            print(max_heap)
            print(res)

            if idx + 1 > len(max_heap):
                idx = 0
            else:
                idx += 1
                




        return len(res)



sol = Solution()
print(sol.leastInterval(["X","X","Y","Y"], 2))
print(sol.leastInterval(["A","A","A","B","C"], 3))