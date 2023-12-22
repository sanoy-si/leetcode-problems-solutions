class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cnt = 0
        water = capacity
        for i in range(len(plants)):
            cnt += 1
            water -= plants[i]
            if i < len(plants) - 1 and water < plants[i+1]:
                cnt += 2 * (i+1)
                water = capacity
        
        return cnt
        