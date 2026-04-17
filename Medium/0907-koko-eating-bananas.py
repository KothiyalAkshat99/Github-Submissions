"""
Problem Name: Koko Eating Bananas
Difficulty: Medium
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 209 ms
Memory: 18.8 MB
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        kmin = 1
        kmax = max(piles)
        k = kmax
        
        def divisible(piles, k):
            s = 0
            for i in piles:
                s += int(ceil(i / k))
            return s
        
        #if n == 1:
            #return divisible(piles, piles[0])
        
        while(kmin <= kmax):
            kmid = (kmin + kmax) // 2
            x = divisible(piles, kmid)
            #print(f"kmid = {kmid}, x = {x}")
            if x > h:
                kmin = kmid + 1
            else:
                if kmid < k:
                    k = kmid
                kmax = kmid - 1
        return k

"""
Submission 2
Language: python3
Runtime: 139 ms
Memory: 18.9 MB
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lwr = 1
        hgr = max(piles) # This is the higher limit for k
        ret = hgr

        def numHours(k) -> bool:
            t = 0 # Count of hours taken at given k
            for i in piles:
                t += ceil(i / k)
            return t
        
        while lwr <= hgr:
            k = (lwr + hgr) // 2
            t = numHours(k)
            print(k)

            if t > h:
                lwr = k + 1
            else:
                ret = min(ret, k)
                hgr = k - 1
        
        return ret

