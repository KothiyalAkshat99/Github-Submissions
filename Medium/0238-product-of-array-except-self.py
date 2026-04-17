"""
Problem Name: Product of Array Except Self
Difficulty: Medium
Tags: Array, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 281 ms
Memory: 26.4 MB
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre, post = list(range(len(nums))), list(range(len(nums)))

        pr = 1
        pst = 1

        for i in range(0, len(nums)):
            pr = pr * nums[i]
            pre[i] = pr
        
        for i in range(len(nums)-1 , -1, -1):
            pst = pst * nums[i]
            post[i] = pst
        
        ret = []

        for i in range(0, len(nums)):
            if i == 0:
                pr = 1
            else:
                pr = pre[i-1]
            if i == len(nums)-1:
                pst = 1
            else:
                pst = post[i+1]
            ret.append(pr*pst)
        
        #print(pre)
        #print(post)

        return ret

"""
Submission 2
Language: python3
Runtime: 39 ms
Memory: 26 MB
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Concept - Pre-fix and Post-fix products

        # Each index is product of all elements upto that index
        # Pre-fix product array -> pref[i] = A[i] * pref[i-1]
        # Post-fix product array -> Similar but from rear end.

        # So for example - 
        # [1, 2, 3, 4]
        # [1, 2, 6, 24] - Pre
        # [24, 24, 12, 4] - Post

        # For value 2 - Prod of elements before 2 is (1) from prefix array
        # Prod of elements after 2 is (12) from postfix array
        # So for 2, results = 1 * 12 = 12

        n = len(nums)
        
        prefix, postfix = [0] * n, [0] * n

        for i in range(0, n):
            if i == 0:
                prefix[i] = nums[i]
                postfix[n-1-i] = nums[n-1-i]
                continue
            prefix[i] = prefix[i - 1] * nums[i]
            postfix[n-1-i] = postfix[n-i] * nums[n-1-i]
        
        ret = [0] * n

        ret[0] = postfix[1]
        ret[n - 1] = prefix[n - 2]

        for i in range(1, n-1):
            ret[i] = prefix[i - 1] * postfix[i + 1]
        
        return ret

"""
Submission 3
Language: python3
Runtime: 19 ms
Memory: 23.2 MB
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums) # Return array does not count for extra memory

        prefix = 1
        for i in range(0, len(nums)):
            ret[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            ret[i] *= postfix
            postfix *= nums[i]
        
        return ret

