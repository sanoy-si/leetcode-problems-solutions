class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        p1 = 0
        p2 = n
        while p2 < len(nums):
            ans.append(nums[p1])
            ans.append(nums[p2])
            p1 += 1
            p2 += 1
            
        return ans

        