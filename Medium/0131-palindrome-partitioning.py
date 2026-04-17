"""
Problem Name: Palindrome Partitioning
Difficulty: Medium
Tags: String, Dynamic Programming, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 46 ms
Memory: 34.5 MB
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        
        ret = []
        part = []

        def backTrack(i):
            if i == len(s):
                ret.append(part[:])
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    backTrack(j+1)
                    part.pop()
        
        backTrack(0)

        return ret
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l +1, r - 1
        return True

"""
Submission 2
Language: python3
Runtime: 39 ms
Memory: 34.4 MB
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        
        ret = []

        def isPalindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        def backtrack(i: str, curpath: str):
            if i == len(s):
                ret.append(curpath[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    curpath.append(s[i : j + 1])
                    backtrack(j + 1, curpath)
                    curpath.pop()
        
        backtrack(0, [])

        return ret

"""
Submission 3
Language: python3
Runtime: 47 ms
Memory: 33.6 MB
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        
        ret = []

        def backtrack(i: str, curpath: str):
            if i == len(s):
                ret.append(curpath[:])
                return
            for j in range(i, len(s)):
                temp = s[i : j + 1]
                if temp == temp[::-1]:
                    curpath.append(s[i : j + 1])
                    backtrack(j + 1, curpath)
                    curpath.pop()
        
        backtrack(0, [])

        return ret

