"""
Problem Name: Prime Number of Set Bits in Binary Representation
Difficulty: Easy
Tags: Math, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 159 ms
Memory: 19.3 MB
"""
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ret = 0
        
        def isPrime(n: int) -> bool:
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        for i in range(left, right + 1):
            setBits = bin(i).count('1')
            if isPrime(setBits):
                ret += 1
        
        return ret


