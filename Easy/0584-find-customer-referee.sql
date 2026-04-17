"""
Problem Name: Find Customer Referee
Difficulty: Easy
Tags: Database
"""

"""
Submission 1
Language: mysql
Runtime: 570 ms
Memory: 0.0B
"""
# Write your MySQL query statement below
SELECT name FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;

