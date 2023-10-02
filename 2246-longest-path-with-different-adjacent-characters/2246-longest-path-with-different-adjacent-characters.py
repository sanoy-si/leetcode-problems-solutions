class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.max = 0
        self.graph = defaultdict(list)
        self.parent = parent
        self.s = s
        for i in range(1,len(parent)):
            self.graph[parent[i]].append(i)
        
        
        
        def dfs(node,pa):
            ma = 0
            sma = 0
            su = 0
            
            for child in self.graph[node]:
                cnt = dfs(child,node)
                if ma <= cnt:
                    sma = ma
                    ma = cnt
                elif sma <= cnt:
                    sma = cnt
                    
            self.max = max(self.max,sma + ma + 1)
            
            if self.s[node] != self.s[pa]:
                return ma + 1
            
            return 0
        
        sma = 0
        ma = 0
        
        for child in self.graph[0]:            
            cnt = dfs(child,0)
            if ma <= cnt:
                sma = ma
                ma = cnt
            elif sma <= cnt:
                sma = cnt

        self.max = max(self.max,sma + ma + 1)
        
        return self.max