"""
Problem Name: Pancake Sorting
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
"""
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # Goal - Iteratively Bring largest unsorted element to correct pos
        # Find index of largest unsorted number
        # Reverse this subarray to move largest to front
        # Flip this array again to move element to correct position.
        # Repeat N times.

        ret = []
        for n in range(len(arr), 1, -1):
            i = arr.index(n)
            if n == i + 1: continue

            if i != 0:
                ret.append(i + 1)
            ret.append(n)

            # Bring largest digit to front
            arr[:i+1] = reversed(arr[:i+1])

            # Move largest number to its final pos
            arr[:n] = reversed(arr[:n])
        
        return ret

