class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ret = False
        new_dict = set(nums)
        print("len", len(new_dict))
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        return ret
        

solution = Solution()
print(solution.containsDuplicate([1,2,3]))