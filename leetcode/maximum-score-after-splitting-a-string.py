class Solution:
    def maxScore(self, s: str) -> int:
        accumulator = 0
        prefix_sum = []
        for i in range(len(s)):
            accumulator += int(s[i])
            prefix_sum.append(accumulator)
        

        accumulator = 0
        postfix_sum = []
        for i in range(len(s) - 1, -1, -1):
            accumulator += int(s[i])
            postfix_sum.append(accumulator)
        
        postfix_sum = postfix_sum[::-1]

        max_answer = 0
        for i in range(len(s) - 1):
            left = (i + 1) - prefix_sum[i]
            right = postfix_sum[i + 1]
            max_answer = max(max_answer, right + left)
        

        return max_answer
        