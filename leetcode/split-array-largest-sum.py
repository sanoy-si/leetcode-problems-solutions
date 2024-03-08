class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def is_valid(num):
            division_count = 1
            curr_sum = 0

            for i in range(len(nums)):
                curr_sum += nums[i]

                if curr_sum > num:
                    division_count += 1
                    curr_sum = nums[i]
            
            return k >= division_count

        left, right = max(nums), sum(nums)
        answer = right
        
        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                answer = mid
                right = mid - 1

            else:
                left = mid + 1

        return answer            