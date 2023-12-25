class Solution(object):
    def pivotArray(self, nums, pivot):
        ln,eq,gn=[],[],[]
        for i in nums:
            if i<pivot:
                ln.append(i)
            elif i==pivot:eq.append(i)
            else:gn.append(i)
        ln.extend(eq)
        ln.extend(gn)
        return ln