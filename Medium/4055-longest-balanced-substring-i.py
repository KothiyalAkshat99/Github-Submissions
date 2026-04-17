"""
Problem Name: Longest Balanced Substring I
Difficulty: Medium
Tags: Hash Table, String, Counting, Enumeration
"""

"""
Submission 1
Language: python3
Runtime: 655 ms
Memory: 19.3 MB
"""
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # Converting to integer
        s = [ord(char) - ord('a') for char in s]
        ret = 0

        for l in range(n):
            if n - l <= ret: # Early exit. Can't be bigger
                break
            
            count = [0] * 26
            uniq = maxFreq = 0

            for r in range(l, n):
                x = s[r]

                if count[x] == 0:
                    uniq += 1
                count[x] += 1

                if count[x] > maxFreq:
                    maxFreq = count[x]
                
                # Current substring length
                curLen = r - l + 1

                # If (num of unique elements) * (max freq of current substring) == current length
                # This means that our criteria of Balanced substring is fulfilled
                # Need to update our balanced substring length if > previous length

                # Basically, if numelements * MaxSubstringFrequency == length
                # This would fail, if for example, some elements DO NOT have freq == MaxFreq
                if uniq * maxFreq == curLen and curLen > ret:
                    ret = curLen
        
        return ret

