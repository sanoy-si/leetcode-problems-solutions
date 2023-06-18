class Solution:
    def reverseParentheses(self, s: str) -> str:
        sta=[]
        for i in s:
            if i==')':
                t=''
                while sta[-1]!='(':
                    t+=sta[-1][::-1]
                    sta.pop()
                sta.pop()
                sta.append(t)
            else:sta.append(i)
        return ''.join(sta)
