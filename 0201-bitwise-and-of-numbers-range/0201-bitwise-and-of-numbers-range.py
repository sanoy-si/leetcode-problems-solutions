class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        answer = 0
        for i in range(30, -1, -1):
            if left & 1 << i != 0 and right & 1 << i != 0:
                answer |= 1 << i

            elif left & 1 << i != 0 or right & 1 << i != 0:
                return answer
            
        return answer


