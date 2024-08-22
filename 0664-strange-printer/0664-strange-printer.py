class Solution:
    def strangePrinter(self, s: str) -> int:
        counter = Counter()
        n = len(s)
        i = 0
        while i < n:
            curr = s[i]
            while i < n and curr == s[i]:
                i += 1
            counter[curr] += 1
        
        chars = sorted('abcdefghijklmnopqrstuvwxyz', key = lambda x: counter[x], reverse = True)
        idxs = defaultdict(list)
        for i in range(n):
            idxs[chars[i]].append(i)

        answer = 0
        added = set()
        for char in chars:
            if counter[char] == 0:
                break
            
            i = 0
            while i < n:
                found = False
                while i < n and char != s[i]:
                    i += 1

                while i < n and s[i] not in added:
                    found = True
                    i += 1

                if found:
                    answer += 1

            added.add(char)

        return answer

            






