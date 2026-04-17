"""
Problem Name: Encode and Decode Strings
Difficulty: Medium
Tags: Array, String, Design
"""

"""
Submission 1
Language: python3
Runtime: 69 ms
Memory: 16.8 MB
"""
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for i in strs:
            x = str(len(i))
            s = s + x + "#" + i
        
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

