class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        if any(nums):
            ones = nums.count(1)
            zeros = len(nums) - ones
        else:
            zeros = len(nums)
            ones = 0
        
        current_zeros = 0
        current_ones = 0
        answer = [0,[]]

        for i in range(len(nums)):
            score = current_zeros + (ones - current_ones)
            if answer [0] < score:
                answer = [score,[i]]
            elif answer[0] == score:
                answer[1].append(i)

            if nums[i] == 0:
                current_zeros += 1
            else:
                current_ones += 1
                
        score = current_zeros + (ones - current_ones)
        if answer [0] < score:
                answer = [score,[len(nums)]]
        elif answer[0] == score:
            answer[1].append(len(nums))

        return answer[1]
        