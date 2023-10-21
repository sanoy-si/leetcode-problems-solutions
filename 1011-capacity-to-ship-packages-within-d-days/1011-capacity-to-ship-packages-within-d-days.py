class Solution:
    def isNum(self, num, weights, days):
        now = 0
        for i in weights:
            if now + i > num:
                days-=1
                now = 0
            if days <= 0: return -1
            now += i
        return 1

        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        print(left,right)
        while left <= right:
            mid = (left + right) // 2
            if self.isNum(mid,weights,days) == 1:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
