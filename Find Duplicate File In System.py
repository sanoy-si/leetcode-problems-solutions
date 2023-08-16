class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in paths:
            files = i.split()
            for j in range(1,len(files)):
                content = files[j].index('(')
                d[files[j][content:]].append(files[0]+'/'+ files[j][:content])
        ans = list(d.values())
        ans = list(filter(lambda x:len(x)>1, ans))
        return ans
