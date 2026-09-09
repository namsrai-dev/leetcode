from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_position = []
        fleet = 1
        for i in range(len(position)):
            new_position.append([position[i], speed[i]])
        new_position.sort(key=lambda x: x[0], reverse=True)
        prev_time = 0
        for idx, i in enumerate(new_position):
            print(idx, i)
            if idx == 0:
                prev_time = (target - i[0]) / i[1]
            else:
                curr_time = (target - i[0]) / i[1]
                print(curr_time, prev_time)
                if curr_time > prev_time:
                    fleet+= 1
                    prev_time = curr_time

        return fleet

# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [(p, s) for p, s in zip(position, speed)]
#         pair.sort(reverse=True)
#         stack = []
#         print(pair)
#         for p, s in pair:  # Reverse Sorted Order
#             print(stack)
#             stack.append((target - p) / s)
#             if len(stack) >= 2 and stack[-1] <= stack[-2]:
#                 stack.pop()
#         return len(stack)

sol = Solution()
print(sol.carFleet(10, [1,4], [3,2]))

sol = Solution()
print(sol.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))