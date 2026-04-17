"""
Problem Name: Bag of Tokens
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 18.1 MB
"""
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        low, high = 0, len(tokens) - 1
        tokens.sort()

        # Lower value tokens played FACE-UP to increase score
        # Higher value tokens played FACE-DOWN to increase power
        while low <= high:
            # Face-Up - We have enough power
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1
            
            # Not enough power to play face-up
            # If atleast 1 token remaining + and enough score, play highest token face-down
            elif low < high and score > 0:
                score -= 1
                power += tokens[high]
                high -= 1
            
            # Not enough score, power or tokens to play face up or down and increase score.
            else:
                return score
        
        return score

