class Solution:
    def decodeString(self, s: str) -> str:
        def decode(beg, end, s):
            ans = []
            p = beg
            while p <= end:
                while p <= end and s[p] not in "123456789":
                    ans.append(s[p])
                    p += 1
                    
                if p > end:
                    return ''.join(ans)
               
                num = []
                while p <= end and s[p] in "1234567890":
                    num.append(s[p])
                    p += 1

                stack = ['[']
                num = int(''.join(num))
                p += 1
                beg = p

                while p <= end and stack:
                    if s[p] == '[':
                        stack.append(s[p])
                    elif s[p] == ']':
                        stack.pop()
                    p += 1

                ans.append(int(num) * decode(beg, p - 2, s))
            
            return ''.join(ans)
        
        return decode(0, len(s) - 1, s)
                
