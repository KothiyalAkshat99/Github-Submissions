"""
Problem Name: Accounts Merge
Difficulty: Medium
Tags: Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 17 ms
Memory: 22.2 MB
"""
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union Find/ Disjointed Sets Union (DSU)
        # UNION by shared emails
        # GROUP emails by Parent
        uf = UnionFind(len(accounts))

        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list)  # index of acc -> list of emails
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        ret = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            ret.append([name] + sorted(emailGroup[i]))
        
        return ret

