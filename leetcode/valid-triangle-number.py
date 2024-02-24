class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums) - 1):
                min_impossible = bisect_left(nums, nums[j] + nums[i])
                ans += max((min_impossible - 1 - j) , 0) 
        
        return ans

                        

