"""
Problem Name: Count Primes
Difficulty: Medium
Tags: Array, Math, Enumeration, Number Theory
"""

"""
Submission 1
Language: python3
Runtime: 1228 ms
Memory: 56.4 MB
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        # SIEVE OF ERATOSTHENES

        # Marks multiples of EACH prime.
        # Leaves only primes

        if n < 2:
            return 0
        
        sieve = [True] * n
        sieve[0] = sieve[1] = False

        i = 2
        while i * i < n:
            if sieve[i]:
                for j in range(i * i, n, i):
                    sieve[j] = False
            i += 1

        return sum(sieve)

