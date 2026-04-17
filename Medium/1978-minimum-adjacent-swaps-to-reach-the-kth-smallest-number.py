"""
Problem Name: Minimum Adjacent Swaps to Reach the Kth Smallest Number
Difficulty: Medium
Tags: Two Pointers, String, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 875 ms
Memory: 17.8 MB
"""
class Solution:
    def findNextPermutation(self, digits):
        i = len(digits) - 1
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
        
        if i == 0: return -1

        j = i
        while j + 1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
    
    def getMinSwaps(self, num: str, k: int) -> int:
        num = list(num)
        perm = num[::]

        # Find kth min permutation
        while k:
            self.findNextPermutation(perm)
            k -= 1
        
        i = ret = 0

        # Number of adjacent swaps required to move from num to perm
        while i < len(num):
            j = i
            while perm[j] != num[i]: j += 1

            while i < j:
                perm[j-1], perm[j] = perm[j], perm[j-1]
                j-=1
                ret += 1
            
            i += 1
        
        return ret

