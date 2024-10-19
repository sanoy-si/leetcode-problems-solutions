class Solution:
    def sn(self,n):
        if n == 1:return '0'
        ini = self.sn(n-1)
        s=[]
        for i in ini:
            if i == '1':s.append('0')
            else:s.append('1')
            
        return ini + '1' + ''.join(s)[::-1]
    
    def findKthBit(self, n: int, k: int) -> str:
        return self.sn(n)[k-1]
        
        
        