# Subsets
# Medium
# Topics
# Company Tags
# Hints
# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [7]

# Output: [[],[7]]
# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
from typing import List


class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def back_track(n):
            pass

        
        back_track(0)
        return arr
    




nums = [1,2,3]

subset = Solution()
subset.subsets(nums)