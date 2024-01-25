class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        psum = [0]
        for num in nums:
            psum.append(psum[-1] + num)

        for i in range(len(nums)):
            if psum[i] == psum[-1] - psum[i + 1]:
                return i
        
        return -1 
        