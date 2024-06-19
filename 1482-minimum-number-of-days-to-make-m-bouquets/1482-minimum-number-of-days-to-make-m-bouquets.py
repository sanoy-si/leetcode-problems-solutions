class Solution:
    def minDays(self, a: List[int], m: int, k: int) -> int:
        if m * k > len(a):
            return -1

        max_days = []
        p = 0
        while p + k <= len(a):
            max_days.append(max(a[p:p + k]))
            p += k
        
        max_days.sort()
        return max_days[m - 1]

        
        
        