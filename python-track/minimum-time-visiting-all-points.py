class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        curr = (points[0][0],points[0][1])
        for x,y in points[1:]:
            ans += max(abs(curr[0]-x),abs(curr[1]-y))
            curr = [x,y]
        
        return ans
        