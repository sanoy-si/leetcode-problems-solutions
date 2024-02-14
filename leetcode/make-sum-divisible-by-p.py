class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
       nums_sum = sum(nums)
       if nums_sum % p == 0:
           return 0

       target = nums_sum % p
       accumulator = 0
       ans = len(nums)
       
       d = {0:-1}
       
       for i, num in enumerate(nums):
           accumulator = (accumulator + num) % p 
           if (accumulator - target) % p in d:
               ans = min(ans, i - d[(accumulator - target) % p])
               
           d[accumulator] = i

       return ans if ans != len(nums) else -1


        

            