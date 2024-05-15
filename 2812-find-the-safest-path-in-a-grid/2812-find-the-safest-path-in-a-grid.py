
class DSU:

    def __init__(self, n):
        self.parent = {(i, j):(i, j) for i in range(n) for j in range(n)}
        self.size = defaultdict(lambda: 1)

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)

        if xp != yp:
            if self.size[xp] >= self.size[yp]:
                 self.parent[yp] = xp
                 self.size[xp] += self.size[yp]

            else:
                 self.parent[xp] = yp
                 self.size[yp] += self.size[xp]


    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])


        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound = lambda i, j: 0 <= i < row and 0 <= j < col
        
        def find_distances():
            distances = {}
            queue = deque([(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1])
            distance = 0
            visited = [[grid[i][j] for j in range(col)] for i in range(row)] 
            
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    distances[(i, j)] = distance

                    for di, dj in dirs:
                        newi, newj = i + di, j + dj
                        if inbound(newi, newj) and not visited[newi][newj]:
                            queue.append((newi, newj))
                            visited[newi][newj] = 1

                distance += 1
            
            return distances
        
        distances = find_distances()

        if (row - 1, col - 1) == (0, 0):
            return grid[0][0] if not grid[0][0] else 0

        distances = sorted(distances.items(), key = lambda x: x[1])

        curr_max = distances[-1][-1]
        lessers = set()
        dsu = DSU(row)

        while distances:
            while distances and distances[-1][-1] == curr_max:
                cell, safeness = distances.pop()
                i, j = cell
                lessers.add(cell)

                for di, dj in dirs:
                    newi, newj = i + di, j + dj
                    if inbound(newi, newj) and (newi, newj) in lessers:
                        dsu.union((i, j), (newi, newj))
                        if dsu.find((0, 0)) == dsu.find((row - 1, col - 1)):
                            return curr_max
            
            curr_max = distances[-1][-1]
                
                        




        



            

            
