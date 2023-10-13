class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = 0
        ma = -1
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr > target and left <= right:
                curr -= nums[left]
                left += 1
            
            if curr == target: ma = max(ma,right - left + 1)
        
        return len(nums) - ma if ma != -1 else ma

        