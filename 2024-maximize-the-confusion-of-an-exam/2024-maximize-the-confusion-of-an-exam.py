class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        ma = 0
        cnt = 0
        # first by True 
        for right in range(len(answerKey)):
            while cnt > k:
                if answerKey[left] == 'F':
                    cnt -= 1
                left += 1
            if answerKey[right] == 'F':
                cnt += 1
            if cnt <= k:
                ma = max(ma,right - left + 1)

        left = 0
        cnt = 0
        # Then by False
        for right in range(len(answerKey)):
            while cnt > k:
                if answerKey[left] == 'T':
                    cnt -= 1
                left += 1
            if answerKey[right] == 'T':
                cnt += 1
            if cnt <= k:
                ma = max(ma,right - left + 1)

        return ma
                