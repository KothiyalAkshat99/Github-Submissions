"""
Problem Name: Verifying an Alien Dictionary
Difficulty: Easy
Tags: Array, Hash Table, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        alpha_map = {}
        for index, char in enumerate(order):
            alpha_map[char] = index

        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]

            for j in range(len(word1)):
                # Looking for FALSE conditions
                if j >= len(word2): return False

                if word1[j] != word2[j]:
                    if alpha_map[word1[j]] > alpha_map[word2[j]]: return False
                    break
        
        return True

