"""
Problem Name: Min Stack
Difficulty: Medium
Tags: Stack, Design
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 21.4 MB
"""
class MinStack:

    def __init__(self):
        self.lst = []
        self.minlst = []

    def push(self, val: int) -> None:
        self.lst.append(val)
        if len(self.minlst) != 0:
            val = min(val, self.minlst[-1])
        self.minlst.append(val)

    def pop(self) -> None:
        self.lst.pop()
        self.minlst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.minlst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Submission 2
Language: python3
Runtime: 5 ms
Memory: 21.3 MB
"""
class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minstk or val <= self.minstk[-1]:
            self.minstk.append(val)

    def pop(self) -> None:
        if self.stk[-1] == self.minstk[-1]:
            self.minstk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 22 MB
"""
class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        
        self.stk.append([val, min_val])

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0] if self.stk else None

    def getMin(self) -> int:
        return self.stk[-1][1] if self.stk else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

