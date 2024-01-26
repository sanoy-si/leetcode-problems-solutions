class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = Counter([0])
        running_sum = 0
        ans = 0

        for num in nums:
            running_sum += num

            ans += counter[running_sum % k]
            ans += counter[-(k - (running_sum % k))]

            counter[running_sum % k] += 1
        
        return ans
