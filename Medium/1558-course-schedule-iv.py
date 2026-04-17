"""
Problem Name: Course Schedule IV
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
"""

"""
Submission 1
Language: python3
Runtime: 32 ms
Memory: 22.5 MB
"""
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = {i:[] for i in range(numCourses)}

        # Need to complete prereq in order to complete course
        for [prereq, course] in prerequisites:
            adj[course].append(prereq)
        
        prereqMap = {}  # {Course->set() of indirect prereqs}
        

        def dfs(course):
            if course not in prereqMap:
                prereqMap[course] = set()
                
                for prereq in adj[course]:
                    prereqMap[course] |= dfs(prereq)    # Union of hashsets
                
                prereqMap[course].add(course)
            
            return prereqMap[course]
        

        for course in range(numCourses):
            dfs(course) # Populate prereqMap for indirect dependencies
        
        ret = []
        for u, v in queries:
            ret.append(u in prereqMap[v])
        
        return ret

