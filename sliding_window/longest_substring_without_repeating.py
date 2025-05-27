class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_arr = []
        ret = 0
        for i in s:
            if i not in window_arr:
                window_arr.append(i)
            else:
                while i in window_arr:
                    window_arr.pop(0)
                window_arr.append(i)
            ret = max(ret, len(window_arr))
        return ret



sol = Solution()
print(sol.lengthOfLongestSubstring("aab"))