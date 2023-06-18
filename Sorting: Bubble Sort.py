def countSwaps(a):
    ln=len(a)
    c=0
    for i in range(ln):
        for j in range(ln-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                c+=1
    print("Array is sorted in {} swaps.".format(c))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[ln-1])) 
