"""
Problem Name: Reconstruct Itinerary
Difficulty: Hard
Tags: Array, String, Depth-First Search, Graph Theory, Sorting, Heap (Priority Queue), Eulerian Circuit
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 20 MB
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # We need to have our adj list in SORTED order
        # But instead of sorting each nb list, we sort the INPUT array
        
        # In reverse -> Can use pop() from end of list
        tickets.sort(reverse = True)
        
        for src, dest in tickets:
            adj[src].append(dest)

        # We stop when len(ret) == len(tickets) + 1
        ret = []
        
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()   # pop lexicographically smallest nb (last element)
                dfs(dest)
            
            # Post-order appending of result -> after all nbs visited
            # Handles dead-ends naturally
            ret.append(src)
        
        dfs("JFK")

        # Path built backwards, so reverse it
        return ret[::-1]

