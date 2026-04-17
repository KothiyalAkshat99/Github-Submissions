"""
Problem Name: Hand of Straights
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 119 ms
Memory: 21 MB
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        hmap = {}
        for i in range(len(hand)):
            num = hand[i]
            if num not in hmap:
                hmap[num] = []
            hmap[num].append(i)
        print(hmap)
        print(hand)
        for i in range(len(hand)):
            num = hand[i]

            if num == -1: # If index has already been used
                continue
            print(f"Num = {num}")
            for j in range(num, num + groupSize):
                print(f"{j} found in hmap")
                if j not in hmap: # if consecutive num not in hmap
                    return False
                temp = hmap[j].pop(0) # Get index of number from hmap
                print(f"{temp} popped from hmap")
                hand[temp] = -1 # Setting index as used
                
                if len(hmap[j]) == 0: # If no more occurences, delete from hmap
                    del hmap[j]
            print("--")
        return True

