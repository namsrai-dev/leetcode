from collections import deque
from typing import List


class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]
        count = 0

        def bfs(i,j):
            q = deque()
            q.append((i, j))

            while q:
                print(q)
                i1, j1 = q.popleft()
                visited[i1][j1] = True
                
                # left
                if j1 - 1 >= 0 and not visited[i1][j1 - 1] and grid[i1][j1 - 1] == "1":
                    q.append((i1, j1 - 1))
                # right
                if j1 + 1 < len(grid[0]) and not visited[i1][j1+1] and grid[i1][j1 + 1] == "1":
                    q.append((i1, j1+1))

                # top
                if i1 > 0 and not visited[i1 - 1][j1] and grid[i1 - 1][j1] == "1":
                    q.append((i1-1, j1))
                # bottom
                if i1 + 1 < len(grid) and not visited[i1 + 1][j1] and grid[i1 + 1][j1] == "1":
                    q.append((i1+1, j1))

        for i, my_list in enumerate(grid):
            for j, item in enumerate(my_list):
                
                if not visited[i][j] and grid[i][j] == "1":
                    print("are you ", i,j)
                    bfs(i,j)
                    count += 1
                    # print("not visited")

        print(visited)

        return count

grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

sol = Solution()
sol.numIslands(grid)