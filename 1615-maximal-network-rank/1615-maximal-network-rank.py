class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for road in roads:
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])
        
        n = 0
        cities = list(graph.keys())
        for i in range(len(cities)):
            for j in range(i+1,len(cities)):
                if cities[i] in graph[cities[j]]:n=max(n,len(graph[cities[i]])-1 + len(graph[cities[j]])-1 +1)
                else:
                    n=max(n,len(graph[cities[i]]) + len(graph[cities[j]]))

        return n