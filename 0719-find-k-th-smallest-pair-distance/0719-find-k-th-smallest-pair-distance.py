class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def check(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                
                count += right - left 

            return count

        left, right = 0, max(nums)
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            result = check(mid)

            if result >= k:
                answer = mid
                right = mid - 1

            else:
                left = mid + 1

        return answer
        
        
        
