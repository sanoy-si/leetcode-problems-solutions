class Solution:
    def freqAlphabets(self, s: str) -> str:
        chars = "abcdefghijklmnopqrstuvwxyz"
        codes = ['1','2','3','4','5','6','7','8','9','10#','11#','12#','13#','14#','15#','16#','17#','18#','19#','20#','21#','22#','23#','24#','25#','26#']
        d = {codes[i]:chars[i] for i in range(26)}
        s = s[::-1]
        p=0
        ans = []
        while p < len(s):
            if s[p] in d:
                ans.append(d[s[p]])
                p+=1
            else:
                ans.append(d[s[p+2]+s[p+1]+s[p]])
                p += 3

        ans = ans[::-1]
        return ''.join(ans)
        