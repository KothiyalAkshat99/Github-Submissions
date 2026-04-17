"""
Problem Name: Next Greater Element II
Difficulty: Medium
Tags: Array, Stack, Monotonic Stack
"""

"""
Submission 1
Language: python3
Runtime: 15 ms
Memory: 19.6 MB
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = [] # Only storing INDICES
        ret = [-1] * n

        # We'll loop through array TWICE
        # Use Stack to store indices whose next greater NOT FOUND
        # Pop from stack while number > top of stack
        
        for i in range(n*2): # Loop through TWICE
            val = nums[i % n]
            while stk and val > nums[stk[-1]]:
                temp = stk.pop()
                ret[temp] = val
            if i < n: stk.append(i) # Adding index onto stack, ONLY ON FIRST ITERATION

        return ret

