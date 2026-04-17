"""
Problem Name: My Calendar I
Difficulty: Medium
Tags: Array, Binary Search, Design, Segment Tree, Ordered Set
"""

"""
Submission 1
Language: python3
Runtime: 175 ms
Memory: 18.6 MB
"""
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        # If no bookings yet
        if not self.bookings:
            self.bookings.append((startTime, endTime))
            return True
        
        # If we already have bookings
        for s, e in self.bookings:
            if e > startTime and s < endTime: # endtime of new booking is before current start time
                return False
        self.bookings.append((startTime,endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

