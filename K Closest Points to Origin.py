def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points=list(sorted(points,key=lambda x:sqrt((x[0]**2)+x[1]**2)))
        return points[0:k]
