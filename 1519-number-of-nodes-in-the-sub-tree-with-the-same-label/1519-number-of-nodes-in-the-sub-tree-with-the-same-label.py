from collections import Counter
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.ans = [0 for i in range(n)]
        self.dict = defaultdict(int)
        self.graph = defaultdict(list)

        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        self.visited = set()

        def dfs(val):
            if not val in self.visited:
                self.visited.add(val)
                counter = Counter()
                counter[labels[val]] = 1
                for child in self.graph[val]:
                    counter += dfs(child)
                self.ans[val] = counter[labels[val]]
                return counter
            return Counter()
        
        dfs(0)
        return self.ans


   