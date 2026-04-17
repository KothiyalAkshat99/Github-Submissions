"""
Problem Name: Letter Case Permutation
Difficulty: Medium
Tags: String, Backtracking, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 5 ms
Memory: 19.3 MB
"""
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # ord() - ordinal - convert char to ascii
        # chr() - convert ascii to character

        res = []
        
        def backtrack(i=0, subst=""):
            if len(subst) == len(s):
                res.append(subst)
            else:
                if s[i].isalpha():
                    backtrack(i + 1, subst + s[i].swapcase())
                backtrack(i + 1, subst + s[i])
        
        backtrack(0, "")
        return res

