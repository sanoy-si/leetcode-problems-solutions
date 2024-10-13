class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))

        heap = [(-1, start_node)]
        probabilities = [inf] * n
        probabilities[start_node] = -1

        while heap:
            probability, node = heappop(heap)
            if node == end_node:
                return -probability
            
            if probability != probabilities[node]:
                continue
            
            for child, weight in graph[node]:
                current_probability = probability * weight
                if probabilities[child] > current_probability:
                    probabilities[child] = current_probability
                    heappush(heap, (current_probability, child))
        
        return 0