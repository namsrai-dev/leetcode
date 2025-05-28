# 424. Longest Repeating Character Replacement
# Attempted
# Medium
# Topics
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_arr = []
        replace_count = 0
        ret = 0
        for i in s:
            if i in window_arr or len(window_arr) == 0:
                window_arr.append(i)
            elif k == 0:
                window_arr = [i]
            else:
                if replace_count < k:
                    replace_count += 1
                else:
                    while replace_count >= k and replace_count > 0:
                        if window_arr.pop(0) != i:
                            replace_count -= 1
            ret = max(ret, len(window_arr) + replace_count)

        return ret


sol = Solution()
# s = "AABABBA", k = 1
print(sol.characterReplacement("BAAA", 0))
