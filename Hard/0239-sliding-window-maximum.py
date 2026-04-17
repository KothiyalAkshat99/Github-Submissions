"""
Problem Name: Sliding Window Maximum
Difficulty: Hard
Tags: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
"""

"""
Submission 1
Language: python3
Runtime: 186 ms
Memory: 31.8 MB
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        l = 0
        r = 0
        q = collections.deque() # index of num, not direct value

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                ret.append(nums[q[0]])
                l += 1
            r += 1

        return ret

"""
Submission 2
Language: python3
Runtime: 191 ms
Memory: 31.2 MB
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonically Decreasing Deque
        # In this deque, leftmost position will always be Current Greatest element
        # Linear time and memory

        ret = []
        left, right = 0, 0
        dq = collections.deque() # Stores indices not direct numbers

        while right < len(nums):
            # Making sure that previous elements in queue are > current element
            # Monotonically decreasing property
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)

            # Shifting the window, checking if leftmost element in dq is out of bounds
            if left > dq[0]:
                dq.popleft()
            
            # Once we have a window of size k, append max value to result
            if (right + 1) >= k:
                ret.append(nums[dq[0]])
                left += 1
            right += 1
        
        return ret

