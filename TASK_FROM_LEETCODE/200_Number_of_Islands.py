from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_graph = {}
        length_grid = len(grid)

        for i in range(length_grid):
            for j in range(length_grid_row := len(grid[i])):
                grid_graph[(i, j)] = []
                zero = []

                if i-1 >= 0:
                    if grid[i-1][j] == '0':
                        zero.append((i-1, j))
                        grid_graph[(i, j)].append((i-1, j))
                    else:
                        grid_graph[(i, j)].append((i-1, j))
                else:
                    zero.append((i-1, j))
                    grid_graph[(i, j)].append((i-1, j))
                
                if i+1 < length_grid:
                    if grid[i+1][j] == '0':
                        zero.append((i+1, j))
                        grid_graph[(i, j)].append((i+1, j))
                    else:
                        grid_graph[(i, j)].append((i+1, j))
                else:
                    zero.append((i+1, j))
                    grid_graph[(i, j)].append((i+1, j))

                if j-1 >= 0:
                    if grid[i][j-1] == '0':
                        zero.append((i, j-1))
                        grid_graph[(i, j)].append((i, j-1))
                    else:
                        grid_graph[(i, j)].append((i, j-1))
                else:
                    zero.append((i, j-1))
                    grid_graph[(i, j)].append((i, j-1))
                
                if j+1 < length_grid_row:
                    if grid[i][j+1] == '0':
                        zero.append((i, j+1))
                        grid_graph[(i, j)].append((i, j+1))
                    else:
                        grid_graph[(i, j)].append((i, j+1))
                else:
                    zero.append((i, j+1))
                    grid_graph[(i, j)].append((i, j+1))

        grid_deque = deque()
        was = set()

        grid_deque += [(0, 0)]
        result = 0

        while grid_deque:
            elem = grid_deque.popleft()
            if elem not in grid_graph:
                continue
            was.add(elem)
            
            for i in grid_graph[elem]:
                if i in was:
                    continue
                
                if i in zero and i not in was:
                    result += 1
                else:
                    grid_deque += [i]
                was.add((i))
            
        return result
    
s = Solution()
a = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(a)

s = Solution()
a = s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print(a)