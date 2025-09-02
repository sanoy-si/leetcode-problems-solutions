class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        answer = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                left, right = sorted([x1, x2])
                bottom, top = sorted([y1, y2])

                if [left, top] != [x1, y1] and [left, top] != [x2, y2]:
                    continue
                    
                valid = True
                for k in range(len(points)):
                    if k in [i, j]:
                        continue
                    
                    if left <= points[k][0] <= right and bottom <= points[k][1] <= top:
                        valid = False
                
                if valid:
                    answer += 1
            
        return answer
                    
