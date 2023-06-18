def insertionSort1(n, arr):
    for i in range(1,n):
        j=i
        t=arr[j]
        while j>0 and t<arr[j-1]:
            arr[j]=arr[j-1]
            print(*arr)
            j-=1
        arr[j]=t
        if j!=i:print(*arr)
        
