class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n, m = len(targetGrid), len(targetGrid[0])
        
        counter = Counter()
        for i in range(n):
            for j in range(m):
                counter[targetGrid[i][j]] += 1
        

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m

        def dfs(i, j):
            count = 0

            stack = [(i, j)]
            val = targetGrid[i][j]
            visited.add((i, j))

            while stack:
                i, j = stack.pop()
                count += 1

                for di, dj in dirs:
                    newi, newj = i + di, j + dj

                    if inbound(newi, newj) and (newi, newj) not in visited and targetGrid[newi][newj] == val:
                        stack.append((newi, newj))
                        visited.add((newi, newj))
                
            return count


        disconnected_colors = set()

        for i in range(n):
            for j in range(n):

                if (i, j) not in visited:
                    count = dfs(i, j)

                    if count != counter[targetGrid[i][j]]:
                        disconnected_colors.add(targetGrid[i][j])
                        
                        if len(disconnected_colors) > 1:
                            return False
        
        return True


        