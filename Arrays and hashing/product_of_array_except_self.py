class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if i != j:
                    num = num * nums[j]
            ret.append(num)
        return ret 



        

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))