"""
Problem Name: Gas Station
Difficulty: Medium
Tags: Array, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 12 ms
Memory: 23.3 MB
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # No solution exists in this case
        if sum(gas) < sum(cost):
            return -1

        # A solution exists 

        ret = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                ret = i + 1
                continue
        # For this starting position, the total never dipped below 0
        # after this position
        return ret

