"""
Problem Name: Swim in Rising Water
Difficulty: Hard
Tags: Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix
"""

"""
Submission 1
Language: python3
Runtime: 31 ms
Memory: 20 MB
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        min_time = float('inf')
        
        pq = [(grid[0][0], 0, 0)]  # Starting from top left

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while pq:
            max_d, r, c = heapq.heappop(pq)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:     # Already reached bottom right
                return max_d
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited:
                    new_d = max(max_d, grid[new_r][new_c])
                    heapq.heappush(pq, (new_d, new_r, new_c))
        
        return -1

