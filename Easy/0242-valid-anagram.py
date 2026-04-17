"""
Problem Name: Valid Anagram
Difficulty: Easy
Tags: Hash Table, String, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 48 ms
Memory: 16.8 MB
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anadict = {}
        for i in s:
            if i not in anadict:
                anadict[i] = 1
            else:
                anadict[i] += 1
        
        for i in t:
            if i in anadict:
                anadict[i] -= 1
            else:
                return False
        
        for i in anadict:
            if anadict[i] != 0:
                return False
        
        return True

"""
Submission 2
Language: python3
Runtime: 11 ms
Memory: 17.9 MB
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        for c in t:
            if c not in hashmap:
                return False
            hashmap[c] -= 1
            if not hashmap[c]: del hashmap[c]
        print(hashmap)
        if hashmap:
            return False
        return True

