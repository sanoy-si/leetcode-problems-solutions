class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        refil = 0
        left,right = 0, len(plants)-1
        self.ca = capacityA
        self.cb = capacityB
        while left < right:
            if capacityA < plants[left]:
                capacityA = self.ca
                refil += 1 
            capacityA -= plants[left]
            left += 1
            
            if capacityB < plants[right]:
                capacityB = self.cb
                refil += 1
            capacityB -= plants[right]
            right -= 1
        
        if left == right:
            if max(capacityA,capacityB) < plants[left]:
                refil += 1
        
        return refil
            
