"""
Problem Name: Integer to Roman
Difficulty: Medium
Tags: Hash Table, Math, String
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.7 MB
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        if  num == 0:
            return ""

        val_sym = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        
        ret = ""

        for val, sym in val_sym:
            if num // val:
                ct = num // val
                ret += (sym * ct)
                num = num % val
        
        return ret

