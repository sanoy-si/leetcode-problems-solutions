class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            closest_complement = float('inf')
            while left < right:
                curr_sum = nums[left] + nums[right]
                # print(curr_sum)
                if abs(closest_complement - (target - nums[i])) > abs(curr_sum - (target - nums[i])):
                    closest_complement = curr_sum

                if curr_sum == target - nums[i]:
                    break

                elif curr_sum < target - nums[i]:
                    left += 1

                else:
                    right -= 1
            print(closest_complement, i)

            if abs(target - closest) > abs(target - (closest_complement + nums[i])):
                        closest = closest_complement + nums[i]
            
        
        return closest
        



        