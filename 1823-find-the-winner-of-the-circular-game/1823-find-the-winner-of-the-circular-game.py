class Solution:
    def rem(self,arr,k):
        ok=k
        if len(arr)==1:return arr[0]
        k-=1
        k%=len(arr)
        arr=arr[k+1:]+arr[0:k]
        return self.rem(arr,ok)
    def findTheWinner(self, n: int, k: int) -> int:
        arr=list(range(1,n+1))
        return self.rem(arr,k)