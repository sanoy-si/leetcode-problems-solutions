class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d=dict(Counter(arr))
        d=list(sorted(list(d.items()),key = lambda x:x[1],reverse = True))
        c=0
        s=0
        ln=len(arr)
        for i in d:
            if s>=ln//2:break
            c+=1
            s+=(i[1])
        return c
