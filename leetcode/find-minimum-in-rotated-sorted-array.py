class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        curr_minimum = nums[0]
        left = 1
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > curr_minimum:
                left = mid + 1
            
            else:
                right = mid - 1
                curr_minimum = nums[mid]
        
        return curr_minimum