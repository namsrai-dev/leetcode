# Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]
# Output: [3,4]

class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        my_dict = {}
        for i in nums1:
            my_dict[i] = True

        for j in nums2:
            if i in my_dict:
                return True
        return False
        

solution = Solution()
solution.findIntersectionValues()