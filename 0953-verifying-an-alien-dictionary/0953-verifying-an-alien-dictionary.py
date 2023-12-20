class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        enum = list(enumerate(order))
        d = {j:i for i,j in enum}
        
        def compare(word1,word2):
            ma = min(len(word1),len(word2))
            for i in range(ma):
                if d[word1[i]] > d[word2[i]]:
                    return True
                elif d[word1[i]] < d[word2[i]]:
                    return False
            return len(word1) > len(word2)
        
        ans = True
        for i in range(len(words)):
            if i < len(words) - 1 and compare(words[i],words[i+1]):
                ans = False
        return ans
            
        
        
        
        