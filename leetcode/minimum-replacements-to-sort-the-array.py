class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            
            number_of_elements = ceil(nums[i] / nums[i + 1])
            ans += number_of_elements - 1
            nums[i] = floor(nums[i] / number_of_elements)
        
        return ans

