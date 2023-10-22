class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if len(people) == 1:return 1
        left, right = 0, len(people) - 1
        requiredBoat = 0
        while left <= right :
            if  people[left] + people[right] <= limit:
                requiredBoat += 1
                left += 1
                right -= 1
            else:
                right -= 1
                requiredBoat += 1
        return requiredBoat

