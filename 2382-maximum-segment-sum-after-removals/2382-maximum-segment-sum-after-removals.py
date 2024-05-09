class DSU:
    def __init__(self, n, nums):
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]
        self.sum = [nums[i] for i in range(n)]
        self.recovered = set()
        self.nums = nums
        self.max = -inf

    def recover(self, idx):

        self.recovered.add(idx)

        self.max = max(self.nums[idx], self.max)

        if idx - 1 in self.recovered:
            self.union(idx, idx - 1)

        if idx + 1 in self.recovered:
            self.union(idx, idx + 1)
        
        return self.max

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)

        if xp != yp:
            if self.size[xp] >= self.size[yp]:
                self.parent[yp] = xp
                self.size[xp] += self.size[yp]
                self.sum[xp] += self.sum[yp]

                self.max = max(self.max, self.sum[xp])
            
            else:
                self.parent[xp] = self.parent[yp]
                self.size[yp] += self.size[xp]
                self.sum[yp] += self.sum[xp]

                self.max = max(self.max, self.sum[yp])

        
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x



class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        answer = [0]
        dsu = DSU(len(nums), nums)

        for idx in removeQueries[::-1]:
            answer.append(dsu.recover(idx))
            print(dsu.parent, dsu.max, dsu.sum, sep = '\n')
        
        return answer[::-1][1:]
