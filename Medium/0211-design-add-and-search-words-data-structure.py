"""
Problem Name: Design Add and Search Words Data Structure
Difficulty: Medium
Tags: String, Depth-First Search, Design, Trie
"""

"""
Submission 1
Language: python3
Runtime: 1254 ms
Memory: 65.6 MB
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        #self.charlist = list(string.ascii_lowercase)

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):

            cur = root

            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child): return True
                    return False
                
                else:
                    if c not in cur.children: return False
                    cur = cur.children[c]
                    
            return cur.endOfWord
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

"""
Submission 2
Language: python3
Runtime: 917 ms
Memory: 69.1 MB
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Initializing 1 root to trie for current object

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # Need to account for WildCard characters (.)
        
        def dfs(idx: int, curr: TrieNode) -> bool:
            
            if idx == len(word):
                return curr.endOfWord
            
            char = word[idx]

            if char == '.':
                # Checking thru all children of current node for wildcard
                for child in curr.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False
            else:
                if char not in curr.children:
                    return False
                return dfs(idx + 1, curr.children[char])
            
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

