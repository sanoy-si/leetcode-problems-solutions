class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = { j:i for i,j in enumerate(nums)}
        for old,new in operations:
            pos = d[old]
            d.pop(old)
            d[new] = pos
        
        ans = [0 ]* len(nums)
        for num,pos in d.items():
            ans[pos] = num

        return ans
        