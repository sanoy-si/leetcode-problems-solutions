class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        ma = len(max(s,key = lambda x: len(x)))
        ans = [[' ' for i in range(len(s))] for j in range(ma)]
        for i in range(len(s)):
            for j in range(ma):
                if j < len(s[i]):
                    ans[j][i] = s [i][j]
        for a in ans:
            while a[-1] == ' ':
                a.pop()
            
        ans = [''.join(a) for a in ans]        
        return ans
        
        