class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num = [int(i) for i in num]
        d = defaultdict(int)
        ans = [0,0,0]
        
        for i in range(3):
            d[num[i]] += 1
            
        if len(d) == 1:
            ans = list(d.keys())
        
        left = 0
        for right in range(3,len(num)):
            d[num[right]] += 1
            d[num[left]] -= 1
            if d[num[left]] == 0:
                d.pop(num[left])
            left += 1
            if len(d) == 1:
                curr = list(d.keys())
                ans = max(curr,ans, key = lambda x: 3 * x[0])
        ans = [str(i) for i in ans]
        return ''.join(ans)*3 if ans != ['0','0','0'] else ""
        