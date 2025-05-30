class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = self.convertDict(s1)
        for i in range(len(s1), len(s2)+1):
            window = s2[i-len(s1):i]
            if set(window) == set(s1):
                window_dict = self.convertDict(window)
                if s1_dict == window_dict:
                    return True
        return False
    
    def convertDict(self, s) -> dict:
        char_count = {}

        for char in s:
            # Use hashmap (dictionary) to count occurrences
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

sol = Solution()
print(sol.checkInclusion("hello", "ooolleoooleh"))
print(sol.checkInclusion("ab", "eidbaooo"))