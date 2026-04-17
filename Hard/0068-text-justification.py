"""
Problem Name: Text Justification
Difficulty: Hard
Tags: Array, String, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []

        newline = []
        curlen = 0

        def justifySpaces(line:list, curlen:int, lastline:bool) -> str:
            remainder = maxWidth - curlen   # Remaining spaces which need to be added
            print(curlen)
            print(remainder)
            n = len(line)   # Number of words in current line
            ret = ""
            # Accoounting for lines with only 1 word, including last line
            if n == 1 or lastline:
                ret = ' '.join(line)
                ret.strip()
                ret += ' ' * remainder
                return ret
            
            # For n > 1 -> Regular justification
            # n words -> n-1 space chunk requirement
            # Need to distribute remainder spaces evenly into n-1 chunks
            spaces = [1 for _ in range(n-1)]  # Total ' ' in between words, including 1 single mandate
            i = 0
            while remainder:
                spaces[i] += 1
                remainder -= 1
                i = (i+1) % (n-1)
            i = 0
            ret += line[0]
            for word in line[1:]:
                ret += ' ' * spaces[i]
                ret += word
                i += 1
            return ret

        for word in words:
            if curlen + len(word) > maxWidth: 
                curlen -= 1     # Remove last space because no longer needed
                justifiedLine = justifySpaces(newline, curlen, False)
                ret.append(justifiedLine)

                # Reset to new line.
                newline = []
                curlen = 0
            
            newline.append(word)
            # +1 for Single space in between words
            curlen += len(word) + 1
        
        # newline is always gonna have stuff after the loop because the last line is still left
        # Need to handle final line now
        curlen -= 1     # Remove added space
        ret.append(justifySpaces(newline, curlen, True))

        return ret

