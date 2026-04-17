"""
Problem Name: Employees Earning More Than Their Managers
Difficulty: Easy
Tags: Database
"""

"""
Submission 1
Language: mysql
Runtime: 429 ms
Memory: 0.0B
"""
# Write your MySQL query statement below
SELECT e.name AS "Employee" FROM Employee e JOIN Employee m ON e.managerid = m.id WHERE e.salary > m.salary;

