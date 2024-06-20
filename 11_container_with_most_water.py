class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        counter = 0

        for idx, h in enumerate(height):

            print(h, idx)

            i = len(height) - 1

            while idx < i:
                counter = counter + 1
                # print('height[i] =>', height[i])
                # print('[i] =>', i)
                min = 0
                if h < height[i]:
                    min = h
                else:
                    min = height[i]

                print(min * (i - idx))
                if (min * (i - idx)) > max:
                    max = min * (i - idx)
                    # i = i - 1
                elif h * (i - idx) < max:
                    i = idx
                else:
                    i = i - 1

        print('max => ', max)
        print('counter => ', counter)



pool = Solution()
pool.maxArea([2,3,4,5,18,17,6])
