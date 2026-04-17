"""
Problem Name: Asteroid Collision
Difficulty: Medium
Tags: Array, Stack, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19 MB
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for ast in asteroids:
            # While new asteroid is moving left and top asteroid is moving right -> Collision
            while stk and stk[-1] > 0 and ast < 0:
                # Stack top smaller
                if stk[-1] < -ast:
                    stk.pop()
                    continue
                
                # Same Size
                elif stk[-1] == -ast:
                    stk.pop()
                    ast = 0
                    break
                
                # Stack top larger. Incoming ast explodes
                else:
                    ast = 0
                    break
            # Only executes if incoming ast survives and is not 0
            if ast:
                stk.append(ast)
        
        return stk

