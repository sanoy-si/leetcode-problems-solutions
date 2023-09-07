class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.num = 0
        n = len(isConnected)
        visited = set()
        self.d = defaultdict(list)
        def dfs(i,visited):
            if i in visited:return 
            visited.add(i)
            for j in self.d[i]:dfs(j,visited)



        for i in range(n):
            s = set()
            for j,k in enumerate(isConnected[i]):
                    if k and j not in s and i != j:
                        s.add(j)
                        self.d[i].append(j)

        for i in range(n):
            print(visited,i)
            if i not in visited:
                dfs(i,visited)
                self.num += 1
        print(self.d)
        return self.num
                        
        
        