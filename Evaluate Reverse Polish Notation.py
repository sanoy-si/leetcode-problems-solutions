class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta=[]
        for i in tokens:
            if i in "+-*/":
                val=eval(sta[-2]+i+sta[-1])
                if val<1 and val>-1:val=0
                elif val<0:val=ceil(val)
                else:val=floor(val)
                sta.pop()
                sta.pop()
                sta.append(str(val))
            else:sta.append(i)
        return int(sta[0])
                
