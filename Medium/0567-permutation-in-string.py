"""
Problem Name: Permutation in String
Difficulty: Medium
Tags: Hash Table, Two Pointers, String, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 2253 ms
Memory: 18 MB
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        hmap1 = {}
        for c in s1:
            hmap1[c] = hmap1.get(c, 0) + 1
        
        # need to check in a window of (len of s1), being run on s2, if that window has exact 
        # same number of characters as are in the first hmap

        l = 0
        r = l1

        while r <= l2:
            hmap2 = {}
            temp = s2[l:r]
            for c in temp:
                hmap2[c] = hmap2.get(c, 0) + 1
            print(f'{hmap1}')
            print('')
            print(f'{hmap2}')
            print('---')
            if hmap1 == hmap2:
                return True
            else:
                l += 1
                r += 1
                continue

        return False

"""
Submission 2
Language: python3
Runtime: 15 ms
Memory: 17.7 MB
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        map1, map2 = {}, {}

        for i in range(len(s1)):
            map1[s1[i]] = 1 + map1.get(s1[i], 0)
            map2[s2[i]] = 1 + map2.get(s2[i], 0)
        
        if map1 == map2:
            return True
        
        left = 0

        # At this point we already have elements in map2 (first window of length(s1))
        for right in range(len(s1), len(s2)):
            map2[s2[right]] = 1 + map2.get(s2[right], 0)
            map2[s2[left]] -= 1

            if map2[s2[left]] == 0:
                del map2[s2[left]]
            left += 1

            if map1 == map2:
                return True
        
        return False

