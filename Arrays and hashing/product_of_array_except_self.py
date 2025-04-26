class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            ret[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1 , -1, -1):
            ret[i] *= postfix
            postfix *= nums[i]
        return ret 



        

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))