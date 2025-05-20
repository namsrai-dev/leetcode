class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            print(l, r)
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: 
                return [l+1, r+1]
        return [l+1, r+1]
    
sol = Solution()    
print(sol.twoSum(numbers=[2,3,4], target=6))