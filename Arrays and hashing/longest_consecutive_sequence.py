from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sorted()
        print(nums)
        return 0


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([2,20,4,10,3,4,5]))