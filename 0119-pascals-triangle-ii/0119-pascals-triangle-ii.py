class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:return[1]
        if rowIndex==1:return[1,1]
        
        ans=[1]+[0] * ( rowIndex-1) +[1]
        ini=self.getRow(rowIndex-1)
        
        for i in range(1,rowIndex):
            ans[i]=ini[i-1]+ini[i]
        return ans