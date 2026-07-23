class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        answer = 1
        while answer <= len(nums):
            answer = answer << 1
        
        return answer

