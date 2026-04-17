"""
Problem Name: Exam Room
Difficulty: Medium
Tags: Design, Heap (Priority Queue), Ordered Set
"""

"""
Submission 1
Language: python3
Runtime: 3770 ms
Memory: 20.4 MB
"""
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.room = [] # Sorted list of occupied seats

    def seat(self) -> int:
        if not self.room:
            self.room.append(0)
            return 0

        newseat = 0
        dist = self.room[0]

        for i in range(len(self.room)-1):
            prevseat = self.room[i]
            nextseat = self.room[i+1]

            currdist = (nextseat - prevseat) // 2

            if currdist > dist:
                dist = currdist
                newseat = prevseat + dist

        lastseat = self.room[-1]
        if self.n - 1 - lastseat > dist:
            newseat = self.n - 1

        bisect.insort(self.room, newseat) # Fast way to insert into sorted list
        return newseat

    def leave(self, p: int) -> None:
        self.room.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

