class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        a_s = []
        b_s = []
        if a > b:
            while a > 0:
                a_s.append('a' * min(a, 2))
                a -= 2

            while b > 0:
                b_s.append('b' * min(b, 1))
                b -= 1
        
        elif a < b:
            while a > 0:
                a_s.append('a' * min(a, 1))
                a -= 1

            while b > 0:
                b_s.append('b' * min(b, 2))
                b -= 2

        else:
            while a > 0:
                a_s.append('a' * min(a, 2))
                a -= 2

            while b > 0:
                b_s.append('b' * min(b, 2))
                b -= 2

        answer = []
        for i in range(min(len(a_s), len(b_s))):
            if len(a_s) > len(b_s):
                answer.append(a_s[i])
                answer.append(b_s[i])
            
            else:
                answer.append(b_s[i])
                answer.append(a_s[i])


        if len(a_s) > len(b_s):
            answer += a_s[len(b_s):]
        
        else:
            answer += b_s[len(a_s):]

        return ''.join(answer)

            