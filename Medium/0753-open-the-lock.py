"""
Problem Name: Open the Lock
Difficulty: Medium
Tags: Array, Hash Table, String, Breadth-First Search
"""

"""
Submission 1
Language: python3
Runtime: 373 ms
Memory: 20.4 MB
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        # Shortest Path Algo - BFS based always

        def children(lock: str) -> List[str]:
            ret = []
            for i in range(4):
                # Case when INCREMENTING digit
                digit = str((int(lock[i]) + 1) % 10)
                ret.append(lock[:i] + digit + lock[i + 1:])

                # Case when DECREMENTING digit
                digit = str((int(lock[i]) - 1 + 10) % 10)
                ret.append(lock[:i] + digit + lock[i + 1:])
            return ret

        dq = deque()
        dq.append(["0000", 0])  # [locks, turns]. Our Starting point of algo
        visited = set(deadends) # Instead of another hash set, add directly to this

        while dq:
            lock, turns = dq.popleft()
            if lock == target:
                return turns
            
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    dq.append([child, turns + 1])
        
        return -1

