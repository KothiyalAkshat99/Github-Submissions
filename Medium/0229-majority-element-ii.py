"""
Problem Name: Majority Element II
Difficulty: Medium
Tags: Array, Hash Table, Sorting, Counting
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 22.4 MB
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        result = set()

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > (len(nums) // 3):
                result.add(num)
        
        return list(result)

"""
Submission 2
Language: python3
Runtime: 3 ms
Memory: 20.5 MB
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # We can only have 2 majority elements with freq > n/3
        n1, n2, c1, c2 = 0, 0, 0, 0

        # Loop to get majority elements without actual count
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 += 1
            elif c2 == 0:
                n2 = num
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1

        c1, c2 = 0, 0
        # Getting actual count of majority elements found
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1

        ret = []
        # Element will only be added if it is indeed in majority
        if c1 > len(nums) // 3:
            ret.append(n1)
        if c2 > len(nums) // 3:
            ret.append(n2)
        
        return ret

