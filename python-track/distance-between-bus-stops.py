class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        psum = [0]
        start,destination = sorted([start,destination])
        for d in distance:
            psum.append(psum[-1]+d)
        return (min(abs(psum[destination]-psum[start]),abs(psum[-1]-psum[destination]+psum[start])))
            
        