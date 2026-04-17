"""
Problem Name: Time Based Key-Value Store
Difficulty: Medium
Tags: Hash Table, String, Binary Search, Design
"""

"""
Submission 1
Language: python3
Runtime: 138 ms
Memory: 75.7 MB
"""
class TimeMap:

    def __init__(self):
        self.tmap = {}
        self.timestamp_prev = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append([timestamp, value])
        return

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        values = self.tmap.get(key, [])

        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l+r) // 2
            if values[mid][0] <= timestamp:
                ret = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return ret


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
Submission 2
Language: python3
Runtime: 159 ms
Memory: 70 MB
"""
class TimeMap:

    def __init__(self):
        self.tmap = {} # Stores key:[timestamp, value] as value
        self.timestamp_prev = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append([timestamp, value])
        return

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        values = self.tmap.get(key, [])

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            # Need to get HIGHEST timestamp_prev <= timestamp
            # Hence shifting to right
            if values[mid][0] <= timestamp:
                ret = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return ret


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

