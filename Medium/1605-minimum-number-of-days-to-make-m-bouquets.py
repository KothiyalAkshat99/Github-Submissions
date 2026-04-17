"""
Problem Name: Minimum Number of Days to Make m Bouquets
Difficulty: Medium
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 316 ms
Memory: 31.5 MB
"""
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        start = min(bloomDay)
        end = max(bloomDay)

        minDays = -1

        # Method to find number of Bouquets that can be made in 'days' no. of days
        def numOfBouquets(days):
            count = 0
            nBouq = 0

            for day in bloomDay:
                if day <= days:
                    count += 1
                else:
                    count = 0
                
                if count == k:
                    nBouq += 1
                    count = 0
            
            return nBouq

        # Binary Search over number of days
        while start <= end:
            mid = (start + end) // 2

            nBouq = numOfBouquets(mid)

            if nBouq >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return minDays

