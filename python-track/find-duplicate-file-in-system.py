class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            path = path.split()
            for i in range(1,len(path)):
                d[path[i][path[i].index('(') + 1 : path[i].index(')')]].append(path[0] + '/' + path[i][:path[i].index('(')])
        
        ans = []
        for key in d:
            if len(d[key]) > 1:
                ans.append(d[key])
            
        return ans