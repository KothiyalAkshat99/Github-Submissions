"""
Problem Name: Cheapest Flights Within K Stops
Difficulty: Medium
Tags: Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 20.6 MB
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for fr, to, prc in flights:
            adj[fr].append((to, prc))
        
        if src not in adj:
            return -1
        
        dist = [float('inf')] * n
        dist[src] = 0
        pq = [(0, (0, src))]   # [stops, (price, node)]

        while pq:
            temp = heapq.heappop(pq)
            currStops, currPrice, currNode = temp[0], temp[1][0], temp[1][1]

            if currStops > k: continue      # If this node exceeds stop limits

            for nb, prc in adj[currNode]:
                if currPrice + prc < dist[nb] and currStops <= k:
                    dist[nb] = currPrice + prc
                    heapq.heappush(pq, (currStops + 1, (currPrice + prc, nb)))
        
        if dist[dst] == float('inf'):
            return -1
        
        return dist[dst]

"""
Submission 2
Language: python3
Runtime: 131 ms
Memory: 20 MB
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0

        for _ in range(k + 1):
            temp = dp[:]

            for flight in flights:
                fl_from = flight[0]
                fl_to = flight[1]
                fl_prc = flight[2]

                # If we can reach starting node of curr flight from source
                if dp[fl_from] != float('inf'):
                    # Update cost to reach destination node of current flight if cheaper
                    temp[fl_to] = min(temp[fl_to], dp[fl_from] + fl_prc)
                
            dp = temp
        
        return dp[dst] if dp[dst] != float('inf') else -1

