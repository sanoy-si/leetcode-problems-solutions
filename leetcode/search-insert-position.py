class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        answer = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
                answer = mid
            
            else:
                left = mid + 1
        
        return answer


        
