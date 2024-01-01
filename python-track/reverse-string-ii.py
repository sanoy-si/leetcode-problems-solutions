class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = []
        flag = True
        ptr = 0
        
        while ptr < len(s):
            if flag:
                answer += s[ptr:min(ptr + k, len(s))][::-1]
                flag = False
            else:
                answer += s[ptr:min(ptr + k, len(s))]
                flag = True

            ptr += k
        
        return ''.join(answer)

        



        