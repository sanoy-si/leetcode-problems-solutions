class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]

       
        def union(x, y):
            x_parent, y_parent = find(x), find(y)

            if x_parent != y_parent:
                if size[x_parent] >= size[y_parent]:
                    parent[y_parent] = x_parent
                    size[x_parent] += size[y_parent]
                
                else:
                    parent[x_parent] = y_parent
                    size[y_parent] += size[x_parent]
            

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        

        answer = n - len([i for i in range(n) if i == find(i)])
        
        return answer


