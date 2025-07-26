class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while r >= l:
            mid = (r + l) // 2
            # print(mid, l, r)
            # print("case", nums[l] < nums[mid] and target >= nums[l] and target < nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[l] < nums[mid]: # when order is l to mid
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]: # when order is mid to r
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                print("gajig", l, mid, r)
                if l == r:
                    return -1
                else:
                    l = mid + 1
        return -1

        

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 3))
print(sol.search([3,1], 0))
# print(sol.search([5,6,7,0,1,2,3,4], 9))
# print(sol.search([5,6,7,3,4], 6))