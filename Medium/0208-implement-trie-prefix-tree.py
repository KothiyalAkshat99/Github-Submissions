"""
Problem Name: Implement Trie (Prefix Tree)
Difficulty: Medium
Tags: Hash Table, String, Design, Trie
"""

"""
Submission 1
Language: python3
Runtime: 39 ms
Memory: 32 MB
"""
# insert each character as child of previous character. 
# Need to mark the final character of each word inserted (e in apple) (no children)
# (root) -> (a) -> (p) -> (p) -> (l) -> (e)

# We mark final character of inserted word so in case of search, for example - \
# We inserted apple. Need to search for word "app".
# 'app' exists as a prefix but p in tree DOES NOT MARK ending of word.
# So returns false
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True # points to last inserted character after loop

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # If last character reached in cur is EOW or not
        return cur.endOfWord 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
Submission 2
Language: python3
Runtime: 31 ms
Memory: 34.2 MB
"""
class TrieNode:
    def __init__(self):
        self.children = {}  # Holds next characters
        self.endOfWord = False  # Check if this node is end of word. Default False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root    # We start from root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()   # Insert new node to current
            curr = curr.children[c]     # Move to the new node
        
        curr.endOfWord = True   # Marks EOW for last char of current inserted word

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]     # Keep moving to next character
        
        return curr.endOfWord   # For last char at curr, check if EOW has been marked

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True     # No need to check EOW. We're only looking for Prefixes

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

