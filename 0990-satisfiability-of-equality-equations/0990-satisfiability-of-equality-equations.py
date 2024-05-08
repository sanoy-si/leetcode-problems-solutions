class DSU:
    
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            if self.size[xp] >= self.size[yp]:
                self.parent[yp] = xp
                self.size[xp] += self.size[yp]

            else:
                self.parent[xp] = yp
                self.size[yp] += self.size[xp]


    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def to_num(char):
            return ord(char) % 97

        dsu =  DSU(26)
        for equation in equations:
            if equation[1] == '=':
                dsu.union(to_num(equation[0]), to_num(equation[3]))
            
            else:
                if dsu.find(to_num(equation[0])) == dsu.find(to_num(equation[3])):
                    return False
            
        
        return True