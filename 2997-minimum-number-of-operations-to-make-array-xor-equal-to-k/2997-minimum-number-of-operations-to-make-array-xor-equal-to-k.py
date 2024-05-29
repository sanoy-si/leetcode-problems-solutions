class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr_bit = 0

        for num in nums:
            for i in range(32):
                if num & 1 << i:
                    curr_bit ^= 1 << i
        
        answer = 0
        while curr_bit or k:
            if curr_bit & 1 != k & 1:
                answer += 1
            
            curr_bit >>= 1 
            k >>= 1
        
        return answer


