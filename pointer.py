class Solution(object):
     def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = float('inf')
        print("float('inf')", float('inf'))
        print("sure ?", nums)
        for i in range(len(nums) - 2):
            print("i", i)
            left, right = i + 1, len(nums) - 1
            while left < right:
                print("left", left)
                print("right", right)
                current_sum = nums[i] + nums[left] + nums[right]
                print("current_sum", current_sum)
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return closest_sum

solution = Solution()
# print(solution.threeSumClosest([-1, 2, -1, 6, -1, 6, 2 -1], -2))
print(solution.threeSumClosest([-4,2,2,3,3,3], 0))
print(solution.threeSumClosest([-1,2,1,-4], 1))
