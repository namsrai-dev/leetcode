
# Example 1:

# Input: nums1 = [2,3,2], nums2 = [1,2]

# Output: [2,1]

# Explanation:



# Example 2:

# Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]

# Output: [3,4]

# Explanation:

# The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.

# The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.

# Example 3:

# Input: nums1 = [3,4,2,3], nums2 = [1,5]

# Output: [0,0]

# Explanation:

# No numbers are common between nums1 and nums2, so answer is [0,0].

 

# Constraints:

# n == nums1.length
# m == nums2.length
# 1 <= n, m <= 100
# 1 <= nums1[i], nums2[i] <= 100


class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer1, answer2 = 0, 0
        for i in range(len(nums1)):
            is_equal = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    is_equal = True
            if is_equal:
                answer1 += 1

        for i in range(len(nums2)):
            is_equal = False
            for j in range(len(nums1)):
                if nums2[i] == nums1[j]:
                    is_equal = True
            if is_equal:
                answer2 += 1
        return [answer1, answer2]
      
        

solution = Solution()
print(solution.findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6]))