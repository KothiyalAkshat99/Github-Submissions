"""
Problem Name: Max Area of Island
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 19 ms
Memory: 19.6 MB
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxarea = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c) -> int:
            if r < 0 or c < 0 \
                or r == rows or c == cols \
                or grid[r][c] != 1 or (r, c) in visited:
                return 0
            
            # Adding current node to visited (Since it is confirmed as 1)
            visited.add((r, c))

            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    temp = dfs(r, c)
                    maxarea = max(maxarea, temp)
        
        return maxarea

"""
Submission 2
Language: python3
Runtime: 27 ms
Memory: 24 MB
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxarea = 0
        visited = set()

        def dfs(r: int, c: int) -> int:
            if r < 0 or r == ROWS or \
                c < 0 or c == COLS or \
                grid[r][c] != 1 or (r, c) in visited:
                return 0
            
            visited.add((r, c))

            ret = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return ret
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxarea = max(maxarea, dfs(r, c))
        
        return maxarea

