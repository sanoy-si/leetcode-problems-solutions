class Solution:
    def decodeString(self, s: str) -> str:
        sta=[]
        ns='1234567890'
        for i in s:
            if i!=']':
                sta.append(i)
            else:
                t=[]
                while sta[-1]!='[':
                    t+=sta[-1]
                    sta.pop()
                sta.pop()
                t=list(reversed(t))
                tt=[]
                while sta and sta[-1] in ns:
                    tt.append(sta[-1])
                    sta.pop()
                tt=''.join(list(reversed(tt)))
                t=int(tt)*t
                sta.extend(t)
        return ''.join(sta)

                
