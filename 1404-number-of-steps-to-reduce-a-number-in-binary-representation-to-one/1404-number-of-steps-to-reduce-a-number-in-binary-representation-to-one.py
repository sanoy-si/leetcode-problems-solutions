class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        s = list(s)
        
        while len(s) > 1:
            if s[-1] == '0':
                s.pop()
                count += 1

            else:
                p = len(s) - 1
                while p >= 0 and s[p] == '1':
                    s[p] = '0'
                    p -= 1

                if p != -1:
                    s[p] = '1'
                    s.pop()
                
                else:
                    s[p + 1] = 1

                count += 2
        
        return count




