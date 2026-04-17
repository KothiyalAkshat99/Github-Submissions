"""
Problem Name: Customer Placing the Largest Number of Orders
Difficulty: Easy
Tags: Database
"""

"""
Submission 1
Language: mysql
Runtime: 468 ms
Memory: 0.0B
"""
# Write your MySQL query statement below
SELECT customer_number 
FROM Orders
GROUP BY customer_number
HAVING COUNT(order_number) = (
    SELECT COUNT(order_number)
    FROM Orders 
    GROUP BY customer_number 
    ORDER BY COUNT(order_number) DESC 
    LIMIT 1);

