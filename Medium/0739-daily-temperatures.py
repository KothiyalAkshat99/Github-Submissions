"""
Problem Name: Daily Temperatures
Difficulty: Medium
Tags: Array, Stack, Monotonic Stack
"""

"""
Submission 1
Language: python3
Runtime: 83 ms
Memory: 27.5 MB
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic Decreasing Stack problem
        st = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)
        return res

"""
Submission 2
Language: python3
Runtime: 95 ms
Memory: 27.5 MB
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        stk = []

        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                idx = stk.pop()
                ret[idx] = i - idx
            
            stk.append(i)
        
        return ret

"""
Submission 3
Language: python3
Runtime: 84 ms
Memory: 27.3 MB
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures) # stores result
        stk = [] # handles stack operations

        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                temp = stk.pop()
                ret[temp] = i - temp

            stk.append(i)
        
        return ret

