"""
Problem Name: Walking Robot Simulation
Difficulty: Medium
Tags: Array, Hash Table, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 24 ms
Memory: 23.7 MB
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # N, E, S, W
        curr_dir = 0    # Index 0 = North, 1 = E, 2 = S, 3 = W
        x, y = 0, 0     # Current pos

        obstacles_set = {tuple(obs) for obs in obstacles}

        max_dist = 0

        for char in commands:
            if char == -1:      # Turn right 90 deg
                curr_dir = (curr_dir + 1) % len(directions)     # or (% 4)
            
            elif char == -2:    # Turn left 90 deg
                curr_dir = (curr_dir + 3) % len(directions)
            
            else:    # Move forward 'char' units, 1 at a time
                dx, dy = directions[curr_dir]
                for _ in range(char):
                    next_x, next_y = x + dx, y + dy

                    if (next_x, next_y) in obstacles_set:
                        break
                    
                    x, y = next_x, next_y
                
                max_dist = max(max_dist, x * x + y * y)
            
        return max_dist

