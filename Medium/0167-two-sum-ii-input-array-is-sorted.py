"""
Problem Name: Two Sum II - Input Array Is Sorted
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 106 ms
Memory: 17.9 MB
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #nums = {i:numbers.index(i) for i in numbers} # HASH APPROACH - not constant space
        #print(nums)
        '''
        j = 0
        i = 0
        for i in num:
            j = target - i
            if j in num:
                i = numbers.index(i)
                j = numbers.index(j)
                print (i, j)
                break
        
        return [i+1, j+1]
        '''

        i = 0
        j = len(numbers)-1
        while i != j:
            x = numbers[i]
            y = numbers[j]
            if x + y == target:
                break
            elif x + y > target:
                j -= 1
            else:
                i += 1

        return [i+1, j+1]

"""
Submission 2
Language: python3
Runtime: 3 ms
Memory: 18.6 MB
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        ret = []

        while left < right:
            n1 = numbers[left]
            n2 = numbers[right]
            if n1 + n2 > target:
                right -= 1
            elif n1 + n2 < target:
                left += 1
            else:
                ret.append(left + 1)
                ret.append(right + 1)
                break
        
        return ret

