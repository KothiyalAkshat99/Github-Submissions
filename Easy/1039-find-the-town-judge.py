"""
Problem Name: Find the Town Judge
Difficulty: Easy
Tags: Array, Hash Table, Graph Theory
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 22.4 MB
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Trust count of each member
        # if a person trusts someone else, that means they do not trust themselves
        # Only the judge has (n-1) incoming trust relationships
        trust_count = [0] * (n + 1)
        
        for (a,b) in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        
        for i in range(1, len(trust_count)):
            if trust_count[i] == n-1:
                return i
        
        return -1

"""
Submission 2
Language: python3
Runtime: 14 ms
Memory: 22.6 MB
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Trust count of each member
        # if a person trusts someone else, that means they do not trust themselves
        # Only the judge has (n-1) incoming trust relationships
        
        if n == 1 and not trust:
            return 1

        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)

        for a,b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(1, n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        
        return -1

