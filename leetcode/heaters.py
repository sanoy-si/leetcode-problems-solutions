class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        max_radius = 0
        for house in houses:
            ind = bisect_left(heaters, house)

            radius = float("inf")

            if ind < len(heaters):
                radius = min(radius, abs(heaters[ind] - house))

            if ind > 0:
                radius = min(radius, abs(heaters[ind - 1] - house))
            
            max_radius = max(radius, max_radius)
        
        return max_radius