class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple[:]
        self.graph = defaultdict(list)
        self.visited = set()
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        
        self.count = 0
        
        def dfs(node):
            if node not in self.visited:
                self.visited.add(node)
                val = False
                for child in self.graph[node]:
                    self.count += 1
                    if dfs(child): 
                        self.count += 1
                        val = True
                    else:self.count -= 1
                    
                if val or self.hasApple[node]:
                    return True
                
                return False
            
        dfs(0)
        return self.count
            
            
        