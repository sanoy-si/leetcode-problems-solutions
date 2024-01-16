class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0
        intersection = []
        while p1 < len(firstList) and p2 < len(secondList):
            curr_intersection = [max(firstList[p1][0], secondList[p2][0]), min(firstList[p1][1], secondList[p2][1])]
            if curr_intersection[0] <= curr_intersection[1]:
                intersection.append(curr_intersection)
            
            if firstList[p1][1] > secondList[p2][1]:
                p2 += 1
            else:
                p1 += 1
        
        return intersection

        