class Solution: 
    def select(self, arr, i):
        n=len(arr)
        mi=i
        for j in range(i+1,n):
            if arr[j]<arr[mi]:mi=j
        return mi
    
    def selectionSort(self, arr,n):
        for i in range(n):
            mi=self.select(arr,i)
            
            arr[i],arr[mi]=arr[mi],arr[i]
        return arr
        
