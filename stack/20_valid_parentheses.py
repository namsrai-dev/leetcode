# 20. Valid Parentheses
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true



# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ret = True
        arr = []
        for i in range(len(s)):
            if arr:
                if self.is_pair(arr[-1], s[i]):
                    arr.pop()
                    continue
            arr.append(s[i])
        if len(arr) != 0:
            ret = False
        print(arr)

        return ret

    def is_pair(self, last, cur):
        if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
            return True
        return False

solution = Solution()
print(solution.isValid("([)])"))
print(solution.isValid("()[]{}"))
