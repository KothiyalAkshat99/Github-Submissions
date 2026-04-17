"""
Problem Name: Circular Array Loop
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 18.1 MB
"""
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def next_index(i):
            return (i + nums[i]) % len(nums)
        
        for i in range(len(nums)):
            slow, fast = i, next_index(i)

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
                
                slow = next_index(slow)
                fast = next_index(next_index(fast))
            
            j = i

            while nums[j] * nums[next_index(j)] > 0:
                temp = j
                j = next_index(j)
                nums[temp] = 0
        return False

