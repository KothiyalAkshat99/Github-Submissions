"""
Problem Name: Course Schedule II
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 20 MB
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {course:[] for course in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        # Need to keep 2 sets
        # visited -> course has been added to output
        visited = set()

        # visiting -> course has not been added to output, but added to Cycle
        visiting = set()

        ret = []

        def dfs(course):
            if course in visiting:
                return False # Course has already been visited previously, cycle detected
            
            if course in visited:
                return True # Course can be completed and added to output
            
            visiting.add(course) # For cycle detection
            
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            
            visited.add(course)
            ret.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return ret

