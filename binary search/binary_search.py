class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)  
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1

# 7 // 2 => 3

# 5 < 13

# l = 5
# r = 6 




sol = Solution()
# print(sol.search([-1,0,3,5,9,12,13], 13))
print(sol.search([-1,0,3,5,9,12,13], 2))
# print(sol.search([5], -5))
# print(sol.search([2,5], 2))

