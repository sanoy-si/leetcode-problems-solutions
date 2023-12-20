class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ma = min(len(word1),len(word2))
        ans = []
        for i in range(ma):
            ans.append(word1[i])
            ans.append(word2[i])
        if len(word1)>ma:
            ans.extend(word1[ma:])
        if len(word2)>ma:
            ans.extend(word2[ma:])
        
        return ''.join(ans)

            
        