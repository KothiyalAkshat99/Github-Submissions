"""
Problem Name: Divide a String Into Groups of Size k
Difficulty: Easy
Tags: String, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
"""
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ngroups = (len(s) // k) if len(s) % k == 0 else (len(s) // k) + 1
        
        ret = []
        while len(s) >= k:
            ret.append(s[0:k])
            s = s[k:]
        
        if s:
            temp = s[0:]
            while len(temp) < k:
                temp += fill
            ret.append(temp)
        
        return ret

