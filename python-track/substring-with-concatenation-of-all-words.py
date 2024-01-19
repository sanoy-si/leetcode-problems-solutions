class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wl = len(words[0])
        sl = len(s)
        wsl = len(words)
        
        answer = []
        target = Counter(words)

        for i in range(wl):
            window = defaultdict(int)
            
            for right in range(i+wl, i + (wsl * wl + 1), wl):
                window[s[right - wl:right]] += 1
            
            if window == target:
                answer.append(i)
            
            left = i
            for right in range(i + (wl * (wsl + 1)), sl+1, wl):
                window[s[right - wl: right]] += 1
                
                window[s[left:left + wl]] -= 1
                if window[s[left:left + wl]] == 0:
                    window.pop(s[left:left + wl])
                
                left += wl
                
                if window == target:
                    answer.append(left)
            
        return answer
                


            
            