class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        curr = 0
        for num in nums:
            curr ^= num
        
        def find_max(curr):
            max_num = 0
            for i in range(maximumBit):
                if curr & 1 << i == 0:
                    max_num |= 1 << i
            
            return max_num

        answer = []
        for i in range(len(nums) - 1, -1, -1):
            answer.append(find_max(curr))
            curr ^= nums[i]
        
        return answer
        
