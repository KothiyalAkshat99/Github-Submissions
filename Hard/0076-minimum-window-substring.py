"""
Problem Name: Minimum Window Substring
Difficulty: Hard
Tags: Hash Table, String, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 61 ms
Memory: 18 MB
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        ct, wndw = {}, {}

        for i in t:
            ct[i] = ct.get(i, 0) + 1
        
        have, need = 0, len(ct)
        ret, retlen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            x = s[r]
            wndw[x] = 1 + wndw.get(x, 0)

            if x in ct and wndw[x] == ct[x]:
                have += 1
            
            while have == need:
                #update result
                if r-l+1 < retlen:
                    ret = [l, r]
                    retlen = r-l+1
                
                wndw[s[l]] -= 1
                if s[l] in ct and wndw[s[l]] < ct[s[l]]:
                    have -= 1
                l+=1
        
        l, r = ret
        return s[l:r+1] if retlen != float("infinity") else ""

"""
Submission 2
Language: python3
Runtime: 71 ms
Memory: 18.2 MB
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(t) > len(s) or not t:
            return ""
        
        hmap_t = Counter(t)
        hmap_s = {}

        n = len(s)
        left, right = 0, 0
        windowlen = float("infinity")
        ret = [-1, -1]
        have, need = 0, len(hmap_t)

        while right < n:
            char = s[right]
            hmap_s[char] = 1 + hmap_s.get(char, 0) # Update element frequency in hashmap

            # If current character is in t and both have same frequency
            if char in hmap_t and hmap_s[char] == hmap_t[char]:
                have += 1
            
            while have == need:
                if right - left + 1 < windowlen:
                    ret = [left, right]
                    windowlen = right - left + 1
                
                hmap_s[s[left]] -= 1
                if s[left] in hmap_t and hmap_s[s[left]] < hmap_t[s[left]]:
                    have -= 1
                
                left += 1
            right += 1
        
        left, right = ret
        return s[left : right + 1] if windowlen != float("infinity") else ""

"""
Submission 3
Language: python3
Runtime: 71 ms
Memory: 18.4 MB
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(t) > len(s) or not t:
            return ""
        
        hmap_t = Counter(t)
        hmap_s = {}

        n = len(s)
        left, right = 0, 0
        windowlen = float("infinity")
        ret = [-1, -1]
        have, need = 0, len(hmap_t)

        while right < n:
            char = s[right]
            hmap_s[char] = 1 + hmap_s.get(char, 0) # Update element frequency in hashmap

            # If current character is in t and both have same frequency
            # Fulfilled frequency count of another character from t in s
            if char in hmap_t and hmap_s[char] == hmap_t[char]:
                have += 1
            
            # While #characters we have fulfilled == #characters we need (t)
            while have == need:
                # Update Results -> If current fulfilled window size < previous window
                if right - left + 1 < windowlen:
                    ret = [left, right]
                    windowlen = right - left + 1
                
                # Moving left index/ window forward by 1
                hmap_s[s[left]] -= 1
                # If char at left index is still a required character but freq count is not equal
                if s[left] in hmap_t and hmap_s[s[left]] < hmap_t[s[left]]:
                    have -= 1
                
                left += 1
            right += 1
        
        left, right = ret
        return s[left : right + 1] if windowlen != float("infinity") else ""

