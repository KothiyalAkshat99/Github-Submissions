"""
Problem Name: Defuse the Bomb
Difficulty: Easy
Tags: Array, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 36 ms
Memory: 16.5 MB
"""
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            code = [0 for i in range(len(code))]
            return code

        n = len(code)

        if k > 0:
            wsum = 0
            i = 1
            for j in range(k):
                wsum += code[i]
                i = (i+1)%n
        
        if k < 0:
            wsum = 0
            i = -1
            kc=k*(-1)
            for j in range(kc):
                wsum += code[i]
                i = -(-(i-1)%n)
                print(i)
        #print(wsum)
        decr_code = []
        decr_code.append(wsum)
        for i in range(1, n):
            if k>0:
                wsum = wsum + code[(i+k)%n] - code[i]
            elif k<0:
                #print(i-1)
                wsum = wsum + code[i-1] - code[-(-(i+k)%n)-1]
                #print(wsum)
                #break
            decr_code.append(wsum)

        return decr_code

