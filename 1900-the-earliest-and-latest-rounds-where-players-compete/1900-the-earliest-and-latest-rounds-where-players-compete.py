class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        def dfs(n, p1, p2):
            if p1 + p2 == n + 1:
                return (1, 1)
            if p1 > p2:
                p1, p2 = p2, p1
            if n <= 4:
                return (2, 2)

            m = (n + 1) // 2
            min_r, max_r = float('inf'), float('-inf')

            if p1 - 1 > n - p2:
                t = n + 1 - p1
                p1 = n + 1 - p2
                p2 = t

            if p2 * 2 <= n + 1:
                a = p1 - 1
                b = p2 - p1 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        r1, r2 = dfs(m, i + 1, i + j + 2)
                        min_r = min(min_r, r1 + 1)
                        max_r = max(max_r, r2 + 1)
            else:
                p4 = n + 1 - p2
                a = p1 - 1
                b = p4 - p1 - 1
                c = p2 - p4 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        offset = i + j + 1 + (c + 1) // 2 + 1
                        r1, r2 = dfs(m, i + 1, offset)
                        min_r = min(min_r, r1 + 1)
                        max_r = max(max_r, r2 + 1)

            return (min_r, max_r)

        return list(dfs(n, firstPlayer, secondPlayer))