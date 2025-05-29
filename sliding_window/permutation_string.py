class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr = list(s1)
        for i in s2:
            if i in s1 and i in s1_arr:
                s1_arr.remove(i)
                if len(s1_arr) == 0:
                    return True
            else:
                s1_arr = list(s1)
            print(s1_arr)
        return False

sol = Solution()
print(sol.checkInclusion("adc", "dcda"))