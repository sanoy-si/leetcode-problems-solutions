class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        def is_palindrome(left, right):
            if left == right:
                return True
            
            if left == right - 1:
                return s[left] == s[right]
            
            if memo[left][right] == -1:
                if s[left] == s[right]:
                    memo[left][right] = is_palindrome(left + 1, right - 1)
                
                else:
                    memo[left][right] = False
            
            return memo[left][right]

            
            
        answer = []
        def func(idx, prev, curr):

            if idx == len(s):
                if curr and curr[-1][-1] == len(s) - 1:
                    answer.append(curr[:])
                
                return
            
            if is_palindrome(prev, idx):
                curr.append((prev, idx))
                func(idx + 1, idx + 1, curr[:])
                curr.pop()
            
            func(idx + 1, prev, curr[:])

        
        func(0, 0, [])

        for i in range(len(answer)):
            for j in range(len(answer[i])):
                left, right = answer[i][j]
                answer[i][j] = s[left:right + 1]

        return answer            

