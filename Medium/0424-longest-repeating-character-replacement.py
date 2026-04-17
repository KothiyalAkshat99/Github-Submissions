"""
Problem Name: Longest Repeating Character Replacement
Difficulty: Medium
Tags: Hash Table, String, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 217 ms
Memory: 18.1 MB
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl = 0
        l, r = 0, 0
        hmap = {}

        def maxfreq(hmap):
            char, count = '', 0
            for c in hmap:
                if hmap[c] > count:
                    char = c
                    count = hmap[c]
            return count
        
        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            
            wnd_len = r - l + 1
            count = maxfreq(hmap)
            
            while (wnd_len - count) > k:
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    del hmap[s[l]]
                l += 1
                wnd_len = r - l + 1
                count = maxfreq(hmap)
            
            maxl = max(maxl, wnd_len)
        
        return maxl

"""
Submission 2
Language: python3
Runtime: 139 ms
Memory: 17.8 MB
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        # Need to expand a window from start.
        # Keep checking max frequency element in current window

        hmap = {}
        ret = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in hmap:
                hmap[s[r]] = 0
            hmap[s[r]] += 1
            maxf = max(hmap.values()) # Max frequency in current window
            curlen = r - l + 1 # Length of window
            
            if curlen - maxf > k: # Checking if 'other' character count exceeds k
                hmap[s[l]] -= 1
                l += 1 # Moving l by 1 position
            
            ret = max(ret, r - l + 1)
        
        return ret

