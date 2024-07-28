class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def with_at_most_k(nums, k):
            if k == 0:
                return 0

            left = right = answer = 0
            counter = Counter()

            for right in range(len(nums)):
                counter[nums[right]] += 1
                while len(counter) > k and left <= right:
                    if counter[nums[left]] == 1:
                        counter.pop(nums[left])

                    else:
                        counter[nums[left]] -= 1
                    
                    left += 1

                answer += right - left + 1

            return answer
        
        return with_at_most_k(nums, k) - with_at_most_k(nums, k - 1)

    