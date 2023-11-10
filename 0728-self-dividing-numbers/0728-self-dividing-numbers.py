class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for num in range(left,right+1):
            answer.append(num)
            for digit in str(num):
                digit = int(digit)
                if digit == 0 or num % digit != 0:
                    answer.pop()
                    break
        
        return answer
                
        