class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,j in enumerate(nums):
            if target - j in d:return[d[target - j], i]
            d[j] = i
            
        
