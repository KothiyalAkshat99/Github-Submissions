"""
Problem Name: 3Sum With Multiplicity
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, Sorting, Counting
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 18 MB
"""
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        count = Counter(arr)

        ret = 0
        i, n = 0, len(arr)

        while i < n:
            j, k = i, n - 1
            while j < k:
                if arr[i] + arr[j] + arr[k] < target:
                    j += count[arr[j]]
                elif arr[i] + arr[j] + arr[k] > target:
                    k -= count[arr[k]]
                else: # when equal to target
                    if arr[i] != arr[j] != arr[k]: # All numbers different
                        ret += count[arr[i]] * count[arr[j]] * count[arr[k]]
                    elif arr[i] == arr[j] != arr[k]: # Smaller 2 nums same
                        ret += count[arr[i]] * (count[arr[i]]-1) * count[arr[k]]//2
                    elif arr[i] != arr[j] == arr[k]: # Larger 2 nums same
                        ret += count[arr[i]] * count[arr[j]] * (count[arr[j]]-1)//2
                    else:   # All nums same
                        ret += count[arr[i]] * (count[arr[i]]-1) * (count[arr[i]]-2)//6
                    j += count[arr[j]]
                    k -= count[arr[k]]
            i += count[arr[i]]
        
        return ret % 1000000007

