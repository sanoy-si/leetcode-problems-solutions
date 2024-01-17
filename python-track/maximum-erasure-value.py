class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = max_score = 0
        counter = defaultdict(int)
        
        left = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            score += nums[right]

            while right - left + 1 > len(counter):
                score -= nums[left]
                counter[nums[left]] -= 1
                
                if counter[nums[left]] == 0:
                    counter.pop(nums[left])
                left += 1
            
            max_score = max(score, max_score)
        
        return max_score

        