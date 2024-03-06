class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starting, ending = -1, -1

        def bisect(mode):
            pos = -1

            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if mode == "left":   
                    if nums[mid] >= target:
                        if nums[mid] == target:
                            pos = mid

                        right = mid - 1

                    else:
                        left = mid + 1
                
                else:
                    if nums[mid] <= target:
                        if nums[mid] == target:
                            pos = mid

                        left = mid + 1

                    else:
                        right = mid - 1
            
            return pos
        
        return [bisect("left"), bisect("right")]