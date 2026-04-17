"""
Problem Name: Minimum Total Distance Traveled
Difficulty: Hard
Tags: Array, Dynamic Programming, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 867 ms
Memory: 50.9 MB
"""
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # SORT robots and factories first by position
        # Allows us to efficiently match each robot to close factory.

        robot.sort()
        factory.sort(key=lambda x: x[0])

        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])
        
        robot_count = len(robot)
        factory_count = len(factory_positions)

        memo = [[0] * (factory_count + 1) for _ in range(robot_count + 1)]
        
        # Initialize base cases
        for i in range(robot_count):
            memo[i][factory_count] = 1e12  # No factories left
        
        # Fill DP table bottom-up
        for i in range(robot_count - 1, -1, -1):
            for j in range(factory_count - 1, -1, -1):
                # Option 1: Assign current robot to current factory
                assign = abs(robot[i] - factory_positions[j]) + memo[i + 1][j + 1]

                # Option 2: Skip current factory for the current robot
                skip = memo[i][j + 1]

                memo[i][j] = min(assign, skip)  # Take the minimum option

        # Minimum distance starting from first robot and factory
        return memo[0][0]  

