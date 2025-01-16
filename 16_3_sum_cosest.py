# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.



# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = None
        for i in range(len(nums) - 2):
            num1 = nums[i]
            for j in range(i+1, len(nums) -1):
                num2 = nums[j]
                for k in range(j+1, len(nums)):
                    num3 = nums[k]
                    sum = num1 + num2 + num3
                    if closest is None:
                            closest = sum
                    else:
                        diff1 = abs(target - closest)
                        diff2 = abs(target - sum)
                        if diff2 <= diff1:
                            closest = sum
        return closest


solution = Solution()
print(solution.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
# print(solution.threeSumClosest([1,2,3,4,5], -2))

