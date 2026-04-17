"""
Problem Name: Sum of All Subset XOR Totals
Difficulty: Easy
Tags: Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration
"""

"""
Submission 1
Language: python3
Runtime: 10 ms
Memory: 19.3 MB
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Backtracking
        # Have 2 choices at each recursive step -> take current element or no

        def backtrack(i: int, xor) -> int:
            if i == len(nums):
                return xor
            
            without_current = backtrack(i + 1, xor)

            with_current = backtrack(i + 1, xor ^ nums[i])

            # Return (with + without) since we require total sum of ALL subsets as the final return value
            return with_current + without_current
        
        return backtrack(0, 0)

