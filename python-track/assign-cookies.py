class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        content_count = 0
        p1 = 0
        p2 = 0

        while p1 < len(g) and p2 < len(s):
            if g[p1] <= s[p2]:
                content_count += 1
                p1 += 1
                p2 += 1

            else:
                p2 += 1
        
        return content_count