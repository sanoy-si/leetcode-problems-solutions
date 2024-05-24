class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        n = len(manager)
        tree = [[] for _ in range(n)]
        
        for i in range(n):
            if i != headID:
                tree[manager[i]].append(i)     

        time_needed = 0
        def dfs(node, current_time):
            nonlocal time_needed
            current_time += informTime[node]
            time_needed = max(time_needed, current_time)   

            for emp in tree[node]:
                dfs(emp, current_time)
        
        dfs(headID, 0)

        return time_needed