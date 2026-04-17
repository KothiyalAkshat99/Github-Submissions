"""
Problem Name: Extra Characters in a String
Difficulty: Medium
Tags: Array, Hash Table, String, Dynamic Programming, Trie
"""

"""
Submission 1
Language: python3
Runtime: 83 ms
Memory: 25 MB
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word: str):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.isEnd = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trieRoot = Trie()
        for word in dictionary:
            trieRoot.insertWord(word)
        trieRoot = trieRoot.root
        
        dp = {len(s): 0}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            
            ret = 1 + dfs(i + 1)    # Skipping current char
            curr = trieRoot
            for j in range(i, len(s)):
                # if current character is not in Trie Prefixes
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isEnd:
                    ret = min(ret, dfs(j + 1))
            dp[i] = ret
            return ret
        
        return dfs(0)

