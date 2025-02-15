
from typing import List

class Solution(object):
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        current = []
        while len(nums) != 0:
            temp = nums.pop()
            while len(current) > 0 and current[len(current) -1] > temp:
                nums.append(current.pop())

            current.append(temp)
        return current



solution = Solution()
print(solution.sortArray([1,3,5,2,4]))