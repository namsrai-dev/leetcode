class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        higher, lower = prices[0], prices[0]
        max_val = 0
        for i in range(1, len(prices)):
            if lower > prices[i]:
                higher, lower = prices[i], prices[i]
            else:
                higher = prices[i]
                max_val = max(max_val, higher - lower)
        return max_val


sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))