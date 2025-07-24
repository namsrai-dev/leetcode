class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while r >= l:
            mid = (r - l) // 2
            print(mid, l, r)
            if mid == target:
                return mid
            elif l < mid and target >= l and target <= r:
                r = mid - 1
            else:
                l = mid + 1
        return -1

        

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 9))