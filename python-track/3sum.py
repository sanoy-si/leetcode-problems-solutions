class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums) - 2):
            sorted_nums = list(sorted(nums[i+1:]))
            left = 0
            right = len(sorted_nums) - 1
            
            print(i,left,right)
            while left < right:
                curr_sum = sorted_nums[left] + sorted_nums[right]
                if curr_sum == -nums[i]:
                    ans.add(tuple(sorted([sorted_nums[left], sorted_nums[right], nums[i]])))
                    left += 1
                    right -= 1

                elif curr_sum < -nums[i]:
                    left += 1

                else:
                    right -= 1
        
        return ans

        