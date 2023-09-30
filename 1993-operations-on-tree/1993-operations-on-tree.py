class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        def func():
            return [[],-1]
        self.graph = defaultdict(func)
        for i in range(1,len(parent)):
            self.graph[parent[i]][0].append(i)

        # return self.graph


        

    def lock(self, num: int, user: int) -> bool:
        if self.graph[num][1] != -1:return False
        self.graph[num][1] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.graph[num][1] == user:
            self.graph[num][1] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def dfs(val):
            if self.graph[val][1] != -1:return False
            if val == num:return True
            for child in self.graph[val][0]:
                if dfs(child):return True
            return False

        def dfs2(val):
            if self.graph[val][1] != -1:return True
            for child in self.graph[val][0]:
                if dfs2(child):return True
            return False
        def dfs3(val):
            self.graph[val][1] = -1
            for child in self.graph[val][0]:
                dfs3(child) 

        if dfs(0):
            passed = False
            for child in self.graph[num][0]:
                if dfs2(child):
                    passed = True
                    break
            if passed:
                self.graph[num][1] = user
                for child in self.graph[num][0]:
                    dfs3(child)
                return True
        return False
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)