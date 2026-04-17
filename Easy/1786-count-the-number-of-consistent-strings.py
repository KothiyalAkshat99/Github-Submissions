"""
Problem Name: Count the Number of Consistent Strings
Difficulty: Easy
Tags: Array, Hash Table, String, Bit Manipulation, Counting
"""

"""
Submission 1
Language: python3
Runtime: 208 ms
Memory: 18.6 MB
"""
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mydict = {}
        for i in allowed:
            mydict[i] = 1
        c = 0
        for i in words:
            flag = 0
            for j in i:
                if j not in mydict:
                    flag = 1
                    break
            if flag == 0:
                c += 1
        
        return c

