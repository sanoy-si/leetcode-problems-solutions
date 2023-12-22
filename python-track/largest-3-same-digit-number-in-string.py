class Solution:
    def largestGoodInteger(self, num: str) -> str:
        counter = defaultdict(int)
        ans = ""
        left = 0
        for right in range(len(num)):
            counter[num[right]] += 1
            while right - left + 1 > 3:
                counter[num[left]] -= 1
                if counter[num[left]] == 0:
                    counter.pop(num[left])
                left += 1
            if right - left + 1 == 3 and len(counter) == 1:
                if not ans or int(ans) < int(num[left:right+1]):
                    ans = num[left:right+1]
        
        return ans