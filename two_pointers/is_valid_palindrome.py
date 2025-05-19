class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(filter(str.isalnum, s)).lower()
        for i in range(len(filtered) // 2):
            if filtered[i] != filtered[len(filtered) - 1 - i]:
                return False
        return True
    
sol = Solution()
# print(sol.isPalindrome("0P"))
print(ord("A"))