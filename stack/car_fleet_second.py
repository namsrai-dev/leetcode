from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_position = []
        fleet = 0
        for i in range(len(position)):
            new_position.append([position[i], speed[i]])
        new_position.sort(key=lambda x: x[0], reverse=True)
        print(new_position)
        i = 0
        while i < target:
            for idx, num in enumerate(new_position):
                if not new_position[idx][0] >= target:
                    pos = new_position[idx][0]
                    speed = new_position[idx][1]
                    if idx == 0:
                        new_position[idx][0] = pos + speed
                    elif pos + speed >= new_position[idx-1][0] and new_position[idx][0] != new_position[idx-1][0]:
                        print("fleet",idx, num)
                        fleet += 1
                        new_position[idx][0] = new_position[idx-1][0]
                        new_position[idx][1] = new_position[idx-1][1]
                    else:
                        new_position[idx][0] = pos + speed

            i+=1
        print("new_position ->",new_position)

        # speed -> [2,2,1,1]
        
        # 0 -> 1 -> 2 -> 3
        # 1 -> 3 -> 5 -> 7
        # 4 -> 6 -> 8 -> 10
        # 7 -> 8 -> 9 -> 10
        return fleet

sol = Solution()
print(sol.carFleet(10, [1,4], [3,2]))

sol = Solution()
print(sol.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))