class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ln=len(piles)
        left=0
        right=ln-1
        s=0
        for i in range(ln//3):
            s+=piles[right-1]
            left+=1
            right-=2
        return s
