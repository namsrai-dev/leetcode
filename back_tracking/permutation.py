# Permutations
# Medium
# Topics
# Company Tags
# Hints
# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [7]

# Output: [[7]]
# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            # print("ret -- ")
            return [[]]

        # print("recursing still", nums)
        perms = self.permute(nums[1:])
        # print("perms", perms)
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        # print("res in first", res)
        return res
    
sol = Solution()
print(sol.permute([1,2,3]))
        