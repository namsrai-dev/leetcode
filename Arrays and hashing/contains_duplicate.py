class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_dict = set(nums)
        if len(new_dict) == len(nums):
            return True
        return False
        

solution = Solution()
print(solution.containsDuplicate([1,2,3]))