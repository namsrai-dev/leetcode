# Kth Largest Element in an Array
# Medium
# Topics
# Company Tags
# Hints
# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

# Follow-up: Can you solve it without sorting?

# Example 1:

# Input: nums = [2,3,1,5,4], k = 2

# Output: 4
# Example 2:

# Input: nums = [2,3,1,1,5,5,4], k = 3

# Output: 4
# Constraints:

# 1 <= k <= nums.length <= 10000
# -1000 <= nums[i] <= 1000



import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        while k > 1:
            heapq.heappop(max_heap)
            k -= 1

        return max_heap[0] * -1




sol = Solution()

print(sol.findKthLargest([2,3,1,1,5,5,4], 3))