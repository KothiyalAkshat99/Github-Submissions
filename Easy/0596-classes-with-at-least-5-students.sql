"""
Problem Name: Classes With at Least 5 Students
Difficulty: Easy
Tags: Database
"""

"""
Submission 1
Language: mysql
Runtime: 302 ms
Memory: 0.0B
"""
SELECT class 
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;

