class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        differentiator = (xor & (xor - 1)) ^ xor
        bucket0, bucket1 = 0, 0
        for num in nums:
            if num & differentiator:
                bucket1 ^= num
            
            else:
                bucket0 ^= num
        
        return [bucket0, bucket1]