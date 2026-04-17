"""
Problem Name: Longest Substring Without Repeating Characters
Difficulty: Medium
Tags: Hash Table, String, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 18.1 MB
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        temp = {}
        start = 0 # beginning of current substring
        for i, c in enumerate(s):
            if c in temp and temp[c] >= start:
                start = temp[c] + 1
            temp[c] = i
            maxlen = max(maxlen, i - start + 1)
        return maxlen

"""
Submission 2
Language: python3
Runtime: 14 ms
Memory: 18 MB
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        
        l, r = 0, 0
        maxlen, curmax = 0, 0
        hset = set()

        while r < len(s):
            x = s[r] # Extract character
            while x in hset:
                hset.remove(s[l])
                l += 1
            
            hset.add(x)
            maxlen = max(maxlen, r-l+1)
            r += 1
        
        return maxlen

"""
Submission 3
Language: python3
Runtime: 11 ms
Memory: 17.9 MB
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hashmap with characters and their last occurence
        # Keep traversing while no duplicates found
        # If duplicate found, move left pointer to index of duplicate stored in HMAP
        # Update max len

        hmap = {}

        l = 0
        maxlen = 0

        for r in range(len(s)):
            x = s[r]

            # if duplicate found AND it is inside current window
            if x in hmap and hmap[x] >= l:
                l = hmap[x] + 1
            
            # Update latest index
            hmap[x] = r

            maxlen = max(maxlen, r - l + 1)
        
        return maxlen

