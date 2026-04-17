"""
Problem Name: Course Schedule
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.5 MB
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TOPOLOGICAL SORT
        # DFS

        # Adjacency List - Prereq map - 
        # HASHMAP -> {Course:[Prereq]}

        # IN DFS approach, we start with first course -> visit neighbours
        # If Neighbour has prereqs, recursively visit prereqs and continue
        # AFTER all neighbours have been visited, add current course
        # This means that in Topological Order, ALL PREREQS have been cleared,
        # and now we can take the course.
        # If any cycle found in between (keep VISITED set), return FALSE

        # Mapping - {COURSE : [PREREQS]}
        # If prereq list empty, means course has no prereqs, can be completed.

        preMap = {i:[] for i in range(numCourses)} # Course:[Prereq]

        for c, pr in prerequisites:
            preMap[c].append(pr)

        visited = set()

        def dfs(course):
            if course in visited:
                return False # cycle found

            if preMap[course] == []:
                return True # Course has no prereqs, can be completed.

            visited.add(course) # Current course has been visited

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            preMap[course] = [] # Marking that course CAN BE COMPLETED
            return True

        # Manually looping through all courses in case of disjointed sets (1->2, 3->4)
        for course in range(numCourses):
            if not dfs(course):
                return False # If for any course cycle is found.
        return True

"""
Submission 2
Language: python3
Runtime: 3 ms
Memory: 21.3 MB
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TOPOLOGICAL SORT

        ## This is our adjacency list. Making sure it has all courses added
        course_prereqs = {i:[] for i in range(numCourses)} # course: [prereqs] 
        
        for [course, prereq] in prerequisites:
            course_prereqs[course].append(prereq)
        
        visited = set()
        
        def dfs(course):
            if not course_prereqs[course]:  # Course has no prereqs
                return True
            if course in visited:   # Cycle found
                return False

            visited.add(course)

            for prereq in course_prereqs[course]:
                if not dfs(prereq):
                    return False
        
            visited.remove(course)
            # At this point, all prereqs have been completed.
            # Hence Marking that this course can be completed now.
            course_prereqs[course] = []

            return True
        
        # Manual loop thru all courses in case of disjointed sets
        for course in range(numCourses):
            if not dfs(course):
                return False    # Returns false only when cycle found.
        
        return True

