# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
        # my_dict = {}
        # res = 0
        # l = r = 0

        # while r < len(s):
        #     if s[r] not in my_dict:
        #         my_dict[s[r]] = 1
        #     else:
        #         my_dict[s[r]] += 1
        #     min_key = 0
        #     max_val = 0
        #     if len(my_dict) > 1:
        #         for key, val in my_dict.items():
        #             max_val+= val
        #             if min_key == 0:
        #                 min_key = val
        #             else:
        #                 min_key = min(min_key, val)
        #     print(my_dict, min_key)
        #     if min_key > k:
        #         my_dict[s[l]] -= 1
        #         l += 1
        #     else:
        #         print(max_val)
        #         res = max(max_val, res)
        #         r += 1
                
        # return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
sol = Solution()

print(sol.characterReplacement("XYYX", 2))
print(sol.characterReplacement("AAABABB", 1))