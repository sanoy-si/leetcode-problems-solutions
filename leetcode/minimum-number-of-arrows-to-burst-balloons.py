class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        lis = []
        
        for point in points:
            if lis:
                lpoint = lis.pop()
                common = [max(point[0], lpoint[0]), min(point[1], lpoint[1])]
                if common[0] <= common[1]:
                    lis.append(common)
                else:
                    lis.append(lpoint)
                    lis.append(point)

            else:
                lis.append(point) 
        
        return len(lis)
        