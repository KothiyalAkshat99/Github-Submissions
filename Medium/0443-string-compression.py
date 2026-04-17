"""
Problem Name: String Compression
Difficulty: Medium
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        n = len(chars)

        i, r = 0, 0

        while r < n:
            char = chars[r]
            c = 0
            while r < n and chars[r] == char:
                c += 1
                r += 1
            
            # Writing character
            chars[i] = char
            i += 1

            if c > 1:
                cstr = str(c)
                for digit in cstr:
                    chars[i] = digit
                    i += 1
        
        return i

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 18.1 MB
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        if len(chars) == 1:
            return 1
        
        left, right = 0, 0
        count = 0
        idx = 0 # Write index
        n = len(chars)

        while right < n:
            char = chars[right]
            count = 0
            while right < n and char == chars[right]:
                count += 1
                right += 1

            chars[idx] = char
            idx += 1
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1
        
        return idx

