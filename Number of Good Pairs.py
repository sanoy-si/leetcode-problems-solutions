class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=0
        c=dict(Counter(nums))
        for i in c:
            t=c[i]-1
            n+=(t*(t+1)/2)
        return int(n)
