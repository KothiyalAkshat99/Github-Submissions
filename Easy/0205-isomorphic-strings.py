"""
Problem Name: Isomorphic Strings
Difficulty: Easy
Tags: Hash Table, String
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 17.9 MB
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return false
        
        # 1 map for S->T mapping, another for T->S mapping
        # So both ways
        # Used to rule out foo->bar and bar->foo mappings
        map1, map2 = {}, {}
    
        for c1, c2 in zip(s, t):
            if (c1 in map1 and map1[c1] != c2) or \
                (c2 in map2 and map2[c2] != c1):
                return False
            map1[c1] = c2
            map2[c2] = c1
        
        return True

