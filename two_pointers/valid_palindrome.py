import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = True
        new_text = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        r = 0
        l = len(new_text) - 1
        for i in range(len(new_text) // 2):
            if(new_text[r] != new_text[l]):
                ret = False
            r+=1
            l-=1
        return ret


sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))