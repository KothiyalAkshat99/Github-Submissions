"""
Problem Name: Combine Two Tables
Difficulty: Easy
Tags: Database
"""

"""
Submission 1
Language: mysql
Runtime: 380 ms
Memory: 0.0B
"""
# Write your MySQL query statement below
SELECT P.firstName, P.lastName, A.city, A.state FROM person P LEFT JOIN address A ON P.personId = A.personId;

"""
Submission 2
Language: mysql
Runtime: 460 ms
Memory: 0.0B
"""
# Write your MySQL query statement below
SELECT P.firstName, P.lastName, A.city, A.state FROM person P LEFT JOIN address A ON P.personId = A.personId;

