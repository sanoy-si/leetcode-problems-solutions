class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.graph[kingName] = [True]
        self.kingName=kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        self.graph[childName].append(True)

    def death(self, name: str) -> None:
        self.graph[name][0] = False
        

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def dfs(name):
            if self.graph[name][0]:
                order.append(name)
            for i in range(1,len(self.graph[name])):
                dfs(self.graph[name][i])
                
        if self.graph[self.kingName][0]:
                order.append(self.kingName)
                
        for i in range(1,len(self.graph[self.kingName])):
            dfs(self.graph[self.kingName][i])
        
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()