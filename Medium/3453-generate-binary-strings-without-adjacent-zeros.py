"""
Problem Name: Generate Binary Strings Without Adjacent Zeros
Difficulty: Medium
Tags: String, Backtracking, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 58 ms
Memory: 19 MB
"""
class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n ==1:
            return ['0', '1']
        ret = []

        def recur(n, st):
            if n == 0:
                ret.append(st[::])
                return
            
            # if last was 0, next digit has to be 1
            if st[-1] == '0':
                recur(n-1, st + "1")
            else:
                recur(n-1, st + "0")
                recur(n-1, st + "1")
            
        recur(n-1, "0")
        recur(n-1, "1")
        return ret

