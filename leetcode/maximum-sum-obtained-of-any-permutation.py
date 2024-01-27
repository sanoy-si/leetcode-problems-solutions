class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        arr = [0 for i in range(len(nums))]
        for left, right in requests:
            arr[left] += 1
            if right < len(nums) - 1:
                arr[right + 1] -= 1

        prefix = []
        accumulator = 0
        for num in arr:
            accumulator += num
            prefix.append(accumulator)

        prefix.sort(reverse=True)
        nums.sort()
        ans = 0
        for num in prefix:
            ans +=  (num * nums.pop())
        
        return int(ans % (1e9 + 7))
