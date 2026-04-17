"""
Problem Name: Not Boring Movies
Difficulty: Easy
Tags: Database
"""

"""
Submission 1
Language: mysql
Runtime: 265 ms
Memory: 0.0B
"""
# Write your MySQL query statement below
SELECT id, movie, description, rating 
FROM Cinema 
WHERE id % 2 <> 0 AND LOWER(description) NOT LIKE 'boring'
ORDER BY rating DESC;

