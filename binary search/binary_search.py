class Solution:
    def search(self, nums: list[int], target: int) -> int:
        is_found = False
        l, r = 0, len(nums)-1
        num_index = (r - l) // 2 + l 
        
        while is_found is not True:
            if nums[num_index] == target:
                return num_index
            elif l == r-1:
                return -1
            elif nums[num_index] < target:
                l = num_index
            else:
                r = num_index
            num_index = (r - l) // 2 + l 





sol = Solution()
print(sol.search([-1,0,3,5,9,12,13], 15))

#  6 // 2 => 3
#  7 // 2 => 3  

# 3, 7 // 2   ->   (7 - 3) / 2 + 3 