class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.lst = [(x,y,r) for x,y,r in bombs]
        self.e = Counter(self.lst)

        self.graph = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:continue
                if sqrt((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2) <= bombs[i][2]:self.graph[i].append(j)

        def dfs(i):
            if i in self.visited1:return 0
            if (bombs[i][0],bombs[i][1]) in self.visited2: return 1

            n=1
            self.visited1.add(i)
            self.visited2.add((bombs[i][0],bombs[i][1]))

            for nei in self.graph[i]:
                n += dfs(nei)
            return n

        lst = []

        for i in range(len(bombs)):
            self.visited1 = set()
            self.visited2 = set()

            lst.append(dfs(i))

        return max(lst)

        