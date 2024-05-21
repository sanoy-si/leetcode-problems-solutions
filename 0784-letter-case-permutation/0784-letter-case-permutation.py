class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        def backtrack(idx, curr):
            if idx == len(s):
                answer.append(''.join(curr))
                return 
            
            if s[idx] not in '0123456789':
                curr.append(s[idx].lower())
                backtrack(idx + 1, curr[:])
                
                curr[-1] = curr[-1].upper()
                backtrack(idx + 1, curr[:])
            
            else:
                curr.append(s[idx])
                backtrack(idx + 1, curr[:])
        
        backtrack(0, [])
    
        return answer
