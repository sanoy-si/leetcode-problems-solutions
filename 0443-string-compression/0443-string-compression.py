class Solution:
    def compress(self, chars: List[str]) -> int:
        def count(i):
            cnt = 0
            val = chars[i]

            while i < len(chars) and chars[i] == val:
                i += 1
                cnt += 1

            return (val,cnt)

        i=0
        n=0
        ans = 0
        while n < len(chars):
            val,icnt = count(n)
            cnt = icnt
            chars[i] = val
            ans += 1
            i += 1
            if cnt > 1:
                for val in str(cnt):
                    chars[i] = val
                    i += 1
                    ans += 1
            n += icnt  
        return ans
        