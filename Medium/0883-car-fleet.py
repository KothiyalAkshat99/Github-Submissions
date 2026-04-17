"""
Problem Name: Car Fleet
Difficulty: Medium
Tags: Array, Stack, Sorting, Monotonic Stack
"""

"""
Submission 1
Language: python3
Runtime: 235 ms
Memory: 39.1 MB
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse Sorted order. Car at closest position to target goes first in this way.
            stack.append((target - p)/ s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: # Means that cars are colliding
                stack.pop()

        return len(stack)

"""
Submission 2
Language: python3
Runtime: 243 ms
Memory: 39.7 MB
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort the Position (+speed) array
        # Makes sense to sort it since they're travelling on same road
        # We will calculate the time each car takes to reach target
        # Take 2 cars at position 0 and 2
        # If car at position 0 potentially reaches target before \
        # car at position 2,
        # means that there would intersect on the way and would become \
        # a fleet eventually somewhere.
        # Important part is the intersection
        # Since car which is lower in position is reaching target before \
        # car which is higher in position

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = [] # Holds time to reach target

        # Reversed sorted order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            # Collision check
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

