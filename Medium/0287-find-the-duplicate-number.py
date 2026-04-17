"""
Problem Name: Find the Duplicate Number
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 32 ms
Memory: 30 MB
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's Cycle Detection

        s = 0
        f = 0

        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s = 0
        while (s != f):
            s = nums[s]
            f = nums[f]

        return s
    

"""
Submission 2
Language: python3
Runtime: 33 ms
Memory: 29.8 MB
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Need to identify that this is a Linked List Problem
        # We are trying to detect entry point of a cycle in a VIRTUAL LINKED LIST derived from array.
        # Treat each INDEX as a NODE.
        # Treat each VALUE at the index as a POINTER to NEXT NODE.
        # This way, duplicated value creates a CYCLE.

        # Floyd's Cycle Detection (TORTOISE AND HARE algo - slow and fast pointers)

        # 2 pointers SLOW and FAST.
        # SLOW ptr moves by 1 hop
        # FAST ptr moves by 2 hops
        # In case of a cycle, both meet somewhere.

        s = 0
        f = 0

        # When cycle found, reset fast ptr, but keep FAST ptr intact for reference.

        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        # RESET SLOW ptr.
        s = 0

        # Move both pointers now at SAME SPEED.
        # The distance between slow(from 0) to start of cycle and 
        # The distance between fast(single hop move) to start of cycle is the same
        while (s != f):
            s = nums[s]
            f = nums[f]

        return s
    

