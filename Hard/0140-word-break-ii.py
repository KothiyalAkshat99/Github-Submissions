"""
Problem Name: Word Break II
Difficulty: Hard
Tags: Array, Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class TrieNode:
    def __init__(self):
        self.children = [None] * 26     # For lowercase English letters
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEnd = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        dp = {}

        # Iterating from end of String
        for i in range(len(s), -1, -1):
            # List to store valid sentences starting from i
            valid_sentences = []

            currnode = trie.root

            # Iterate from i to end of string
            for j in range(i, len(s)):
                char = s[j]
                idx = ord(char) - ord("a")

                # Check if curr char in trie
                if not currnode.children[idx]:
                    break
                
                # Move to next node
                currnode = currnode.children[idx]

                if currnode.isEnd:
                    currword = s[i:j+1]

                    if j == len(s) - 1:
                        valid_sentences.append(currword)
                    else:
                        sentences_from_next_index = dp.get(j + 1, [])
                        for sentence in sentences_from_next_index:
                            valid_sentences.append(
                                currword + " " + sentence
                            )
            dp[i] = valid_sentences
        
        return dp.get(0, [])

