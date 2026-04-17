"""
Problem Name: Employees Whose Manager Left the Company
Difficulty: Easy
Tags: Database
"""

"""
Submission 1
Language: mysql
Runtime: 343 ms
Memory: 0.0B
"""
# Write your MySQL query statement below
SELECT employee_id FROM Employees
WHERE salary < 30000 and manager_id IN (SELECT manager_id FROM Employees WHERE manager_id NOT IN (SELECT employee_id FROM Employees))
ORDER BY employee_id ASC;

"""
Submission 2
Language: mysql
Runtime: 340 ms
Memory: 0.0B
"""
# Write your MySQL query statement below
SELECT 
    e.employee_id
FROM 
    Employees e
LEFT JOIN 
    Employees m
    ON e.manager_id = m.employee_id
WHERE 
    e.salary < 30000
    AND e.manager_id IS NOT NULL
    AND m.employee_id IS NULL
ORDER BY 
    e.employee_id;

