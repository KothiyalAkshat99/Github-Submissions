"""
Problem Name: Group Anagrams
Difficulty: Medium
Tags: Array, Hash Table, String, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 88 ms
Memory: 19.3 MB
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) == 1:
            return [strs]
        
        mydict = {}

        for i in strs:
            j = ''.join(sorted(i))
            if j in mydict:
                mydict[j].append(i)
            else:
                mydict[j] = [i]

        ret = []

        for i in mydict:
            ret.append(mydict[i])
        
        return ret

"""
Submission 2
Language: python3
Runtime: 82 ms
Memory: 19.4 MB
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) == 1:
            return [strs]
        
        mydict = {}

        for i in strs:
            j = ''.join(sorted(i))
            if j in mydict:
                mydict[j].append(i)
            else:
                mydict[j] = [i]

        ret = [mydict[i] for i in mydict]
        
        return ret

"""
Submission 3
Language: python3
Runtime: 11 ms
Memory: 20.3 MB
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or len(strs) == 1:
            return [strs]

        hmap = {}

        for word in strs:
            word_sort = "".join(sorted(word))
            if word_sort not in hmap:
                hmap[word_sort] = [word]
            else:
                hmap[word_sort].append(word)
        
        return list(hmap.values())

