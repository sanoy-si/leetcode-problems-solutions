class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        d = {}
        for i,num  in enumerate(nums):
            d[(i+k)%n] = num
            
        for i,n in d.items():
            nums[i] = n
        
        
        