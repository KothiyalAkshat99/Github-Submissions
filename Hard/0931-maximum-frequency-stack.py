"""
Problem Name: Maximum Frequency Stack
Difficulty: Hard
Tags: Hash Table, Stack, Design, Ordered Set
"""

"""
Submission 1
Language: python3
Runtime: 82 ms
Memory: 28.1 MB
"""
class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxCount = 0
        self.stack = {} # Stack of stacks (Count -> Elements)

    def push(self, val: int) -> None:
        valCount = self.count.get(val, 0) + 1
        self.count[val] = valCount

        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stack[valCount] = []
        
        self.stack[valCount].append(val)

    def pop(self) -> int:
        ret = self.stack[self.maxCount].pop()
        self.count[ret] -= 1
        if not self.stack[self.maxCount]:
            self.maxCount -= 1
        return ret

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

