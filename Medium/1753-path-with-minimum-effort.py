"""
Problem Name: Path With Minimum Effort
Difficulty: Medium
Tags: Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix
"""

"""
Submission 1
Language: python3
Runtime: 1371 ms
Memory: 21.3 MB
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS, COLS = len(heights), len(heights[0])

        dq = deque()
        dq.append((0,0))    # Starting from Top Left

        cost = {(row, col): float('inf') for col in range(COLS) for row in range(ROWS)}
        cost[(0,0)] = 0

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            r, c = dq.popleft()
            curr_height = heights[r][c] # Current node height
            curr_cost = cost[(r, c)]    # Current node cost

            for d_r, d_c in directions:
                row = r + d_r
                col = c + d_c

                if 0 <= row < ROWS and 0 <= col < COLS:
                    nb_height = heights[row][col]   # Get new neighbour's height
                    new_cost = max(curr_cost, abs(nb_height - curr_height))

                    if new_cost < cost[(row, col)]:
                        cost[(row, col)] = new_cost
                        dq.append((row, col))
        
        return cost[(ROWS - 1, COLS - 1)]

"""
Submission 2
Language: python3
Runtime: 296 ms
Memory: 21.7 MB
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS, COLS = len(heights), len(heights[0])

        # Using minHeap instead of deque
        minHeap = [(0, 0, 0)]   # (distance, row, col), starting from top left

        cost = {(row, col): float('inf') for col in range(COLS) for row in range(ROWS)}
        cost[(0,0)] = 0

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            curr_height = heights[r][c]

            if r == ROWS - 1 and c == COLS - 1:
                return d    # Reached bottom right

            for d_r, d_c in directions:
                row = r + d_r
                col = c + d_c

                if 0 <= row < ROWS and 0 <= col < COLS:
                    nb_height = heights[row][col]   # Get new neighbour's height
                    
                    # If neighbour height is lower/higher than current height
                    new_cost = max(d, abs(nb_height - curr_height))     

                    if new_cost < cost[(row, col)]:
                        cost[(row, col)] = new_cost
                        heapq.heappush(minHeap, (cost[(row, col)], row, col))

