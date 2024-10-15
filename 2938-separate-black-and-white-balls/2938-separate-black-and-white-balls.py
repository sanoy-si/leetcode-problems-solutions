class Solution:
    def minimumSteps(self, s: str) -> int:
        pos = len(s) - 1
        answer = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                answer += abs(pos - i)
                pos -= 1
        
        return answer