"""
Problem Name: Flipping an Image
Difficulty: Easy
Tags: Array, Two Pointers, Bit Manipulation, Matrix, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
"""
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        if not image:
            return image
        
        rows = len(image)
        cols = len(image[0])
        
        for i in range(rows):
            left = 0
            right = cols - 1
            while left <= right:
                image[i][left], image[i][right] = image[i][right] ^ 1, image[i][left] ^ 1
                left += 1
                right -= 1
        return image

