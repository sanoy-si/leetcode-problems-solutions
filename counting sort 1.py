def countingSort(arr):
    flist=[0]*100
    for i in range(max(arr)+1):
        flist[i]=arr.count(i)
    return flist
