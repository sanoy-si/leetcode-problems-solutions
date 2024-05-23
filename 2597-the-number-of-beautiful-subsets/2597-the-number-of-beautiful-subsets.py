class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        answer = 0
        nums.sort()
        counter = Counter()

        def backtrack(idx, taken):
            nonlocal answer 

            if idx == len(nums):
                answer += 1
                return 
            
            take, dont_take = 0, 0
            if idx != len(nums) - 1 or taken:
                backtrack(idx + 1, taken)
            
            if counter[nums[idx] - k] == 0:
                counter[nums[idx]] += 1
                backtrack(idx + 1, True)
                counter[nums[idx]] -= 1

        backtrack(0, False)

        return answer 
            