"""
Problem Name: Minimum Obstacle Removal to Reach Corner
Difficulty: Hard
Tags: Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 1068 ms
Memory: 42.9 MB
"""
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # Min Cost Path - DJIKSTRA
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        ROWS, COLS = len(grid), len(grid[0])

        # Distance matrix
        min_obstacles = [[float('inf')] * COLS for _ in range(ROWS)]
        min_obstacles[0][0] = grid[0][0]
        
        # priority queue
        pq = [(min_obstacles[0][0], 0, 0)]  # (obstacles, row, col)

        while pq:
            obs, row, col = heapq.heappop(pq)

            if row == ROWS - 1 and col == COLS - 1: # If we've reached bottom right
                return obs
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    new_obs = obs + grid[new_row][new_col]

                    if new_obs < min_obstacles[new_row][new_col]:
                        min_obstacles[new_row][new_col] = new_obs
                        heapq.heappush(pq, (new_obs, new_row, new_col))
        
        return min_obstacles[ROWS - 1][COLS - 1]

