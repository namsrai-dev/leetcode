class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        my_dict = {}
        ret = []
        for i in nums:
            if i not in my_dict:
                my_dict[i] = True
            else:
                ret.append(i)
        return ret
