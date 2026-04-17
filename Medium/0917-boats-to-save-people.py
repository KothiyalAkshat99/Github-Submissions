"""
Problem Name: Boats to Save People
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 42 ms
Memory: 23.3 MB
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people:
            return 0
        # GREEDY

        people.sort()

        left = 0
        right = len(people) - 1

        ret = 0

        while left <= right:
            remaining = limit - people[right]
            right -= 1
            ret += 1
            if left <= right and remaining >= people[left]:
                left += 1
            
        return ret

"""
Submission 2
Language: python3
Runtime: 43 ms
Memory: 23.3 MB
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        
        people.sort() # n log n
        boats = 0
        n = len(people)
        left, right = 0, n - 1
        
        while left <= right:
            # Fitting heavier people first
            remaining = limit - people[right]
            right -= 1
            boats += 1
            if left <= right and remaining >= people[left]:
                left += 1

        return boats

