class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {j:i for i,j in enumerate(nums)}
        for i,j in operations:
            d[j] = d[i]
            d.pop(i)
        ans =[None] * len(nums)
        for i,j in d.items():
            ans[j] = i
        return ans
