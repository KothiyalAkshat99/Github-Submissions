"""
Problem Name: Next Greater Element III
Difficulty: Medium
Tags: Math, Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Same Logic as Next Permutation.
        # Find index i where number at [i-1] < [i], starting from the end.
        # Now, starting from i, find j s.t. number at [j] is JUST larger than [i-1]
        # Swap [i-1] and [j]
        # Reverse everything AFTER i [i:][::-1]
        # That is the next permutation
        digits = list(str(n))

        i = len(digits) - 1
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
        
        if i == 0: return -1

        j = i
        while j + 1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))

        return ret if ret < 1 << 31 else -1

