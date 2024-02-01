class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 1001

        for num, left, right in trips:
            passengers[left] += num
            passengers[right] -= num
        
        accumulator = 0
        for i in range(1000):
            accumulator += passengers[i]
            passengers[i] = accumulator


        return max(passengers) <= capacity