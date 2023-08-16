class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        newString = []
        for i in range(len(s)):
            if i in spaces:newString.append(' ')
            newString.append(s[i])
        return ''.join(newString)
                
                
        
