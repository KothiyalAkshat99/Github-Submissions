"""
Problem Name: Simplify Path
Difficulty: Medium
Tags: String, Stack
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 18.1 MB
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        ret = ""
        l = 0
        if path[-1] != "/": path += "/"
        n = len(path)
        print(path)

        for r in range(1, n):
            x = path[r]
            if x == '/':
                if r == l + 1:
                    l = r
                    continue
                dr = path[l +  1: r]
                if dr == "..":
                    if stk: stk.pop()
                elif dr == ".":
                    pass
                else:
                    stk.append(dr)
                l = r
        print(stk)
        for dr in stk:
            ret += "/" + dr
        
        return ret if ret else "/"

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        splits = path.split("/")

        for split in splits:
            if split == "" or split == ".":
                continue
            
            if split == "..":
                if stk: stk.pop()
            
            else:
                stk.append(split)
        
        return "/" + "/".join(stk)

