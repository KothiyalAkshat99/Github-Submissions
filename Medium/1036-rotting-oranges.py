"""
Problem Name: Rotting Oranges
Difficulty: Medium
Tags: Array, Breadth-First Search, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.5 MB
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1 # Keeping track of number of total fresh oranges
                if grid[r][c] == 2:
                    q.append([r,c]) # Appending coordinates of initial rotten oranges in mtrx
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # if in bounds and fresh, make rotten
                    if (row < 0 or row == len(grid) or \
                        col < 0 or col == len(grid[0]) or\
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

"""
Submission 2
Language: python3
Runtime: 3 ms
Memory: 19.4 MB
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi-Source BFS
        # Allows to start from ALL rotten oranges simultaneously

        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0
        fresh = 0
        dq = deque()

        # Adding all rotten oranges to deque.
        # Also keep track of fresh oranges (for final check)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    dq.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        # BFS
        while dq and fresh > 0:
            
            # Process the entire current "layer" (all oranges for this minute)
            for _ in range(len(dq)):
                r, c = dq.popleft()
                
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = r + dr, c + dc

                    # If inbound and neighbour is fresh, mark rotten
                    if (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        dq.append((row, col))
            
            minutes += 1
        
        if not fresh:
            return minutes
        else:
            return -1

