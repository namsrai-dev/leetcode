class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ret = []
        for i in range(k-1, len(nums)):
            max_num = float('-inf')
            for j in range(k):
                max_num = max(max_num, nums[i-j])
            ret.append(max_num)

        return ret


sol = Solution()
print(sol.maxSlidingWindow([1], 1))