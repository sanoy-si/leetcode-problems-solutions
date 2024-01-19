class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_ans = 0
        
        # first by True 
        cnt = 0
        left = 0
        for right in range(len(answerKey)):
            while cnt > k:
                if answerKey[left] == 'F':
                    cnt -= 1
                left += 1
            if answerKey[right] == 'F':
                cnt += 1
            if cnt <= k:
                max_ans = max(max_ans,right - left + 1)

        # Then by False
        left = 0
        cnt = 0
        for right in range(len(answerKey)):
            while cnt > k:
                if answerKey[left] == 'T':
                    cnt -= 1
                left += 1
            if answerKey[right] == 'T':
                cnt += 1
            if cnt <= k:
                max_ans = max(max_ans,right - left + 1)

        return max_ans
                
