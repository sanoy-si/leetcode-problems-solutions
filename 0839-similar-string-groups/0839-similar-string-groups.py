
class DSU:

    def __init__(self, words):
        self.parent = {i:i for i in words}
        self.size = defaultdict(lambda: 1)

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
    def numSimilarGroups(self, strs: List[str]) -> int:
        dsu = DSU(strs)
        n = len(strs)

        def is_valid(word1, word2):
            difference = {}
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    difference[word1[i]] = word2[i]
            
            if difference and len(difference) != 2:
                return False

            keys = list(difference.keys())
            return difference[keys[0]] == keys[1] and difference[keys[1]] == keys[0] 

        for i in range(n):
            for j in range(i + 1, n):
                if is_valid(strs[i], strs[j]):
                    dsu.union(strs[i], strs[j])
        
        answer = 0
        for word in strs:
            if dsu.parent[word] == word:
                answer += 1
        
        return answer
        