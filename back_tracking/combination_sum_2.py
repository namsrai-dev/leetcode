# Combination Sum II
# Medium
# Topics
# Company Tags
# Hints
# You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input: candidates = [9,2,2,4,6,1,5], target = 8

# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]
# Example 2:

# Input: candidates = [1,2,3,4,5], target = 7

# Output: [
#   [1,2,4],
#   [2,5],
#   [3,4]
# ]
# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ret = []

        def arr_sum(my_arr):
            total_sum = 0
            for i in my_arr:
                total_sum += i
            return total_sum

        def dfs(arr1, arr2):
            if arr_sum(arr2) == target:
                ret.append(arr2)
                # return
            
            for i, num in enumerate(arr1):
                new_arr = arr2.copy()
                new_arr.append(num)
                if arr_sum(new_arr) <= target:
                    dfs(arr1[i+1:], new_arr)

        index = 0

        while len(nums) > index:
            # print(nums[index])
            dfs(nums[index+1:], [nums[index]])
            if len(nums) > index + 1 and nums[index + 1] == nums[index]:
                index+=1    
            index+=1

        # for i, num in enumerate(nums):
        #     dfs(nums[i+1:], [num])

        return ret


sol = Solution()

print(sol.combinationSum([1,2,3,4,5], 7))