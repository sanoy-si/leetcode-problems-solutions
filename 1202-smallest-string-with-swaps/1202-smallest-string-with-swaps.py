class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        graph = defaultdict(list)

        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a) 

        
        groups = []
        visited = set()

        def dfs(i):
            group = []

            stack = [i]
            visited.add(i)

            while stack:
                node = stack.pop()
                group.append(node)

                for nei in graph[node]:
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)
        
            groups.append(group) 



        for i in range(len(s)):
            if i not in visited:
                dfs(i)
        
        idx_pair = {}

        for group in groups:
            chars = [s[i] for i in group]
            group.sort()
            chars.sort()

            for i in range(len(group)):
                idx_pair[group[i]] = chars[i]
        
        answer = [idx_pair[i] for i in range(len(s))]

        return ''.join(answer)