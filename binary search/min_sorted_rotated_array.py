class Solution:
    def findMin(self, nums: list[int]) -> int:
        return sorted(nums)[0]


sol = Solution()
print(sol.findMin([3,4,5,1,2]))