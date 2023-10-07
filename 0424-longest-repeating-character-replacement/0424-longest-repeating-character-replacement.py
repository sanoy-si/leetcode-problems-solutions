class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        counter = Counter(s)
        mk = k
        
        for char in counter.keys():
            left = 0
            cnt = 0
            k = mk
            for right in range(len(s)):
                if k > 0 or char == s[right]:
                    if char != s[right]:
                        k-=1
                    cnt += 1
                else:
                    while k == 0:
                        if s[left] != char:
                            k+=1
                        left+=1
                        cnt -= 1
                    cnt += 1
                    k=0
                ans = max(ans,cnt)
        return ans 


                

        