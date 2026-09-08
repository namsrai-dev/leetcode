class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_speed = speed
        i = 0
        new_position = sorted(position)
        while i < target:
            for i in new_position:
                print

            i+=1
        # speed -> [2,2,1,1]
        
        # 0 -> 1 -> 2 -> 3
        # 1 -> 3 -> 5 -> 7
        # 4 -> 6 -> 8 -> 10
        # 7 -> 8 -> 9 -> 10
        return 0
