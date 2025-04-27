class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        max = 1
        count = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                count += 1
            else:
                count = 1
            if count > max:
                max = count
        return max



sol = Solution()
print(sol.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))