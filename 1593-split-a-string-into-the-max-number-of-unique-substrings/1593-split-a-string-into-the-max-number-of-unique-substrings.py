class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        added = set()
        answer = 0
        def backtrack(idx):
            nonlocal answer
            if idx == len(s):
                answer = max(answer, len(added))
                return
            
            for i in range(idx + 1, len(s) + 1):
                if len(added) + (len(s) - i) < answer:
                    break

                if s[idx:i] not in added:
                    added.add(s[idx:i])
                    backtrack(i)
                    added.remove(s[idx:i])

        backtrack(0)

        return answer

