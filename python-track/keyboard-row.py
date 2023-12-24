class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 ="qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        ans = []
        for word in words:
            possible = True
            
            if word[0].lower() in row1:
                row = row1
            elif word[0].lower() in row2:
                row = row2
            else:
                row = row3
            for char in word:
                if char.lower() not in row:
                    possible = False
                    
            if possible:
                ans.append(word)
                
        return ans
        