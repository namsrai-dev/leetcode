class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_dict = {}
        ret = []
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        for l in range(k):
            max = 0
            max_idx = 0
            for i in my_dict:
                if my_dict[i] > max:
                    max = my_dict[i]
                    max_idx = i
            ret.append(max_idx)
            my_dict.pop(max_idx)
        return ret
        

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))