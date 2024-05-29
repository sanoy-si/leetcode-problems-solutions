class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        carry = 0

        if len(a) > len(b):
            b = ((len(a) - len(b)) * '0') + b
        
        else:
            a = ((len(b) - len(a)) * '0') + a

        a = list(map(int, a))
        b = list(map(int, b))

        p = len(a) - 1

        while p >= 0:
            if not a[p] and not b[p]:
                if carry:
                    answer.append(1)
                    carry = 0
                
                else:
                    answer.append(0)
            
            elif a[p] and b[p]:
                if carry:
                    answer.append(1)
                
                else:
                    answer.append(0)
                    carry = 1
            
            else:
                if carry:
                    answer.append(0)

                else:
                    answer.append(1)
            
            p -= 1
        
        if carry:
            answer.append(1)

        answer = list(map(str, answer))
        
        return ''.join(answer[::-1])                


       