class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for i in range(len(classes)):
            passing, total = classes[i]
            curr = passing / total
            new = (passing + 1) / (total + 1)
            heappush(heap, (-(new - curr), i))
        
        for _ in range(extraStudents):
            _, i = heappop(heap)
            classes[i] = [classes[i][0] + 1, classes[i][1] + 1]
            curr = classes[i][0] / classes[i][1]
            new = (classes[i][0] + 1) / (classes[i][1] + 1)
            heappush(heap, (-(new - curr), i))
        
        tot = 0
        for passing, total in classes:
            tot += passing / total
        
        return tot / len(classes)
            