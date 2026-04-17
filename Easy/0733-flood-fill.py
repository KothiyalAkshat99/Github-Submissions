"""
Problem Name: Flood Fill
Difficulty: Easy
Tags: Array, Depth-First Search, Breadth-First Search, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def recur(self, image, sr, sc, t, color):
        rows, cols = len(image), len(image[0])
        if sr < 0 or sr >= rows or sc < 0 or sc >= cols or image[sr][sc] != t:
            return
        
        image[sr][sc] = color

        self.recur(image, sr-1, sc, t, color)
        self.recur(image, sr+1, sc, t, color)
        self.recur(image, sr, sc-1, t, color)
        self.recur(image, sr, sc+1, t, color)
            
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image: return [[]]
        t = image[sr][sc]

        if t == color:
            return image
        
        self.recur(image, sr, sc, t, color)

        return image

