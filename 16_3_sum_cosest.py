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
        closest = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            print("i =>", i)
            left = i + 1
            right = len(nums) - 1
            while right > left:
                print(i, left, right)
                num1 = nums[i]
                num2 = nums[right]
                num3 = nums[left]
                sum = num1 + num2 + num3
                print("sum =>",sum)
                diff1 = abs(closest - target)
                diff2 = abs(sum - target)
                print("diff1 =>",diff1)
                print("diff2 =>",diff2)
                if diff2 < diff1:
                    closest = sum
                if sum < target:
                     left += 1
                     print("left --", left)
                elif sum > target:
                     right -= 1
                     print("right ++", right)
                else:
                     return sum
        return closest


solution = Solution()
# print(solution.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
# print(solution.threeSumClosest([1,2,3,4,5], -2))
print(solution.threeSumClosest([-1,2,1,-4], 1))

