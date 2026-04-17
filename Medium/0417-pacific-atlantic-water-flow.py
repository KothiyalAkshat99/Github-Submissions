"""
Problem Name: Pacific Atlantic Water Flow
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 36 ms
Memory: 19.4 MB
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ''' 
        Basic Approach is that initially, entirety of -
        FIRST ROW and FIRST COLUMN always flows into PACIFIC
        LAST ROW and LAST COLUMN always flows into ATLANTIC

        We're trying to go in reverse order.
        We're taking the first/last rows/cols, & trying to find cells of SAME/INCREASING height        
        '''
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        ret = []

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or \
                r < 0 or c < 0 or r == ROWS or c == COLS or \
                heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        # First and LAST ROW
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        # FIRST and LAST COL
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    ret.append([r, c])
        
        return ret

"""
Submission 2
Language: python3
Runtime: 35 ms
Memory: 22.3 MB
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visited_pcf, visited_atl = set(), set()
        ret = []

        def dfs(r: int, c: int, visited: set, prevHeight: int):
            if r == ROWS or c == COLS or \
                r < 0 or c < 0 or \
                (r, c) in visited or \
                heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        
        # For FIRST and LAST rows -> Traversing over all cols
        # FIRST ROW -> Pacific
        # LAST ROW -> Atlanta 
        for c in range(COLS):
            dfs(0, c, visited_pcf, heights[0][c])
            dfs(ROWS - 1, c, visited_atl, heights[ROWS-1][c])
        
        # For FIRST and LAST cols -> Traversing over all rows
        for r in range(ROWS):
            dfs(r, 0, visited_pcf, heights[r][0])
            dfs(r, COLS - 1, visited_atl, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited_pcf and (r, c) in visited_atl:
                    ret.append([r, c])
        
        return ret

