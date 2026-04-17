"""
Problem Name: Maximum Number of Weeks for Which You Can Work
Difficulty: Medium
Tags: Array, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 31.1 MB
"""
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # There's 2 cases - 

        # CASE 1 
        # We take the project with maximum milestones -> [1(A), 2(B), 3(C)].
        # We take 3 = C
        # -> C _ C _ C
        # We need 2 others to fill in the gaps
        # S = Sum of other projects (A+B) = 1 + 2 = 3
        # -> C A C B C B
        # All projects can be completed when Sum(all other milestones) >= Max(milestones) - 1
        # Total weeks = SUM(all milestones)
        
        # CASE 2
        # When Sum of ALL OTHER PROJECTS < Max(milestones)
        # In this case the largest project cannot be completed fully (Due to consecutive week constraint)
        # Here, max milestones which can be completed from LARGEST project = S + 1
        # S here denotes sum of all other milestones (except largest)
        # So finally, total weeks = S + S + 1 = 2S + 1

        # Final formula = min(2S + 1, sum(all milestones)) 
        # Includes both cases

        total_sum = sum(milestones)
        max_val = max(milestones)
        others_sum = total_sum - max_val

        return min(2 * others_sum + 1, total_sum)

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 31.1 MB
"""
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # There's 2 cases - 

        # CASE 1 
        # We take the project with maximum milestones -> [1(A), 2(B), 3(C)].
        # We take 3 = C
        # -> C _ C _ C
        # We need 2 others to fill in the gaps
        # S = Sum of other projects (A+B) = 1 + 2 = 3
        # -> C A C B C B
        # All projects can be completed when Sum(all other milestones) >= Max(milestones) - 1
        # Total weeks = SUM(all milestones)
        
        # CASE 2
        # When Sum of ALL OTHER PROJECTS < Max(milestones)
        # In this case the largest project cannot be completed fully (Due to consecutive week constraint)
        # Here, max milestones which can be completed from LARGEST project = S + 1
        # S here denotes sum of all other milestones (except largest)
        # So finally, total weeks = S + S + 1 = 2S + 1

        # Final formula = min(2S + 1, sum(all milestones)) 
        # Includes both cases

        total_sum = sum(milestones)
        max_val = max(milestones)
        others_sum = total_sum - max_val

        #return min(2 * others_sum + 1, total_sum)

        # Return simplification ->
        
        if max_val > others_sum + 1:    # Case 2: Limited by largest project
            return 2 * others_sum + 1
        
        return total_sum    # Case 1: Can finish everything
        

