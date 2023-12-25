class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = [i for i in range(len(boxes)) if boxes[i] == '1']
        answer = []
        for i in range(len(boxes)):
            ops = 0
            for j in ones:
                ops += abs(j - i)
            answer.append(ops)
        
        return answer
        