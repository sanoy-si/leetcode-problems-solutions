class Solution:
    def minWindow(self, s: str, t: str) -> str:
       tcounter = Counter(t)
       window = Counter()
       
       min_len = float('inf')
       ans = ""
       left = 0
       for right in range(len(s)):
            window[s[right]] += 1
            
            while tcounter - window == Counter():
               if min_len > right - left + 1:
                    ans = s[left: right+1]

               window[s[left]] -= 1

               min_len = min(min_len, right - left + 1)
               
               left += 1
           

       return ans