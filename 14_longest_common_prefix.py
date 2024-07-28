# 14. Longest Common Prefix
# Easy
# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution(object):
    def longestCommonPrefix(self, strs):
        ret = strs[0]
        for i in range(1, len(strs)):
            str1 = strs[i-1]
            str2 = strs[i]
            if i == 1:
                ret = getMatchedString(str1, str2)
            elif ret == "":
                return ret
            else:
                ret = getMatchedString(ret, str2)
        return ret



def getMatchedString(str1, str2):
    min = len(str1)
    addstr = ""
    if(min > len(str2)):
        min = len(str2)
    for i in range(min):
        if (str1[i] == str2[i]):
            addstr += str1[i]
        else:
            return addstr
    return addstr





Solution().longestCommonPrefix(["flower","flow","flight"])

