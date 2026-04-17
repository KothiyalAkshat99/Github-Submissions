"""
Problem Name: Word Search II
Difficulty: Hard
Tags: Array, String, Backtracking, Trie, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 6586 ms
Memory: 19.2 MB
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Make TRIE with input words
        # Search while dfs-ing + backtracking?

        '''
        For each position in graph, start greedy search and
        check if current character is in Trie. If no, move to next word.
        If yes, move recursively to adjacent positions and check if they are
        children of parent node.
        '''

        root = TrieNode()

        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])

        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or \
                r == rows or c == cols or \
                (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            
            visit.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)

"""
Submission 2
Language: python3
Runtime: 6439 ms
Memory: 21.2 MB
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        trieRoot = Trie()
        for word in words:
            trieRoot.insertWord(word)
        trieRoot = trieRoot.root

        ret, visited = set(), set()

        def dfs(r: int, c: int, node: Trie, word: str) -> None:
            if r == ROWS or r < 0 or \
                c == COLS or c < 0 or \
                (r, c) in visited or \
                board[r][c] not in node.children:
                return
            
            # Add current character 
            visited.add((r,c))
            # Since board[r][c] is in node.children (as found in base case)
            node = node.children[board[r][c]]   
            word += board[r][c]

            # If the current position in Trie forms a word, add to result
            if node.isEnd:
                ret.add(word[::])

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trieRoot.children:
                    dfs(r, c, trieRoot, "")
        
        return list(ret)

