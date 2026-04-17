"""
Problem Name: Letter Combinations of a Phone Number
Difficulty: Medium
Tags: Hash Table, String, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ret = []

        map = {"2":["a", "b", "c"],
                "3":["d", "e", "f"],
                "4":["g", "h", "i"],
                "5":["j", "k", "l"],
                "6":["m", "n", "o"],
                "7":["p", "q", "r", "s"],
                "8":["t", "u", "v"],
                "9":["w", "x", "y", "z"]
                }

        def bt(idx, st):
            if idx == len(digits):
                ret.append(st[:])
                return
            
            digit = digits[idx]
            chars = map[digit]

            for char in chars:
                st += char
                bt(idx+1, st)
                st = st[:len(st)-1]
        
        bt(0, "")

        return ret

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ret = []

        # {Digit:[characters]}
        map = {"2":["a", "b", "c"],
                "3":["d", "e", "f"],
                "4":["g", "h", "i"],
                "5":["j", "k", "l"],
                "6":["m", "n", "o"],
                "7":["p", "q", "r", "s"],
                "8":["t", "u", "v"],
                "9":["w", "x", "y", "z"]
                }

        # Recursively going over string indices
        def bt(idx, st):
            if idx == len(digits): # If final index reached
                ret.append(st[:])
                return
            
            # Getting current digit and its character map
            digit = digits[idx]
            chars = map[digit]

            # Iterating over all characters of current digit
            for char in chars:
                st += char  # including current 'character'
                bt(idx+1, st)   # recursive call to next 'digit'
                st = st[:len(st)-1]     # popping current 'character'
        
        bt(0, "")

        return ret

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 19.6 MB
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        ret = []

        def backtrack(i: int, st: str) -> None:
            if i == len(digits):
                ret.append(st[::])
                return
            
            for char in num_map[digits[i]]:
                st += char  # Add character to current string
                backtrack(i + 1, st)    
                st = st[:len(st) - 1]   # Pop character from current string
        
        backtrack(0, "")

        return ret

