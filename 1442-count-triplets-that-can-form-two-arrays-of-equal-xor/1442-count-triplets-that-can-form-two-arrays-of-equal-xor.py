class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)

        answer = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                for k in range(j, n + 1):
                    if prefix[j - 1] ^ prefix[i - 1] == prefix[k] ^ prefix[j - 1]:
                        answer += 1
        
        return answer
