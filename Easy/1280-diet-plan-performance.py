"""
Problem Name: Diet Plan Performance
Difficulty: Easy
Tags: Array, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 152 ms
Memory: 26.3 MB
"""
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        totalcal = sum(calories[:k])
        score = 0

        if totalcal > upper:
            score += 1
        elif totalcal < lower:
            score -= 1

        for i in range(k, len(calories)):
            #print(i)
            #print(calories[i])
            #print(totalcal)

            totalcal = totalcal + calories[i] - calories[i-k]

            if totalcal > upper:
                score += 1
                #print(f"yes {score}")
            elif totalcal < lower:
                score -= 1
                #print(f"no {score}")
            else:
                #print(f"ignored {score}")
                continue
        
        return score

