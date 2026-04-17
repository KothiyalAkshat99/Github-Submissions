"""
Problem Name: Word Ladder
Difficulty: Hard
Tags: Hash Table, String, Breadth-First Search
"""

"""
Submission 1
Language: python3
Runtime: 51 ms
Memory: 22.6 MB
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # For each word, track how many characters differ from other words
        # hit -> hot(1), dot(2), dog(3), lot(2), log(3), cog(3)
        # hot -> dot(1), dog(2), lot(1), log(2), cog(2)
        # dot -> dog(1), lot(1), log(2), cog(2)
        # dog -> lot(2), log(1), cog(1)
        # Need to get first word with 1 difference
        # Also need to check if at any stage, endWord is in reach (difference of 1)
        # Okay above approach is wrong (not entirely)

        ### Approach is -> Adj List + BFS for SHORTEST PATH

        nbs = collections.defaultdict(list)     # {Pattern:[words]}
        wordList.append(beginWord)

        for word in wordList:   # Creating adjacency List
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nbs[pattern].append(word)
        
        visited = set([beginWord])
        dq = deque([beginWord])
        ret = 1     # final length. Start with 1 since we're at beginWord

        # So we start with beginWord, build its patterns, get all its neighbours
        # Then we Go into each of its neighbours
        # Layer by Layer
        # Hence BFS

        while dq:
            for i in range(len(dq)):
                word = dq.popleft()
                if word == endWord:
                    return ret
                
                for j in range(len(word)):  # Get neighbours of word by building its patterns
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nb in nbs[pattern]:
                        if nb not in visited:
                            visited.add(nb)
                            dq.append(nb)

            ret += 1
        
        return 0

