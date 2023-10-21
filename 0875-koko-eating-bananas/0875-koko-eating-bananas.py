class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ma=max(piles)
        left=1
        right=ma
        mv=0
        while left<=right:
            m=(left+right)//2
            if self.is_valid(m,piles,h):
                right=m-1
                mv=m
            else:left=m+1
        return mv
    def is_valid(self,num,piles,h):
            te=0
            v=True
            for i in piles:
                te+=(ceil(i/num))
                if te>h:
                    v=False
                    break
            if v:return 1
            return 0
        


