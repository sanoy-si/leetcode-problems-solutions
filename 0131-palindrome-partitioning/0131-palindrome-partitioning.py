class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        memo = [[False for _ in range(len(s))] for _ in range(len(s))]
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

            
            
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

