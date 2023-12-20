class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1,5,10,50,100,500,1000]
        d = {symbols[i]:values[i] for i in range(7)}
        ans = 0
        for i  in range(len(s)):
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
        return ans
        
        
        