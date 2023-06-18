def countingValleys(steps, path):
    s=0
    c=0
    for i in path:
        if s==0 and i=='D':
            c+=1
        if i=='D':s-=1
        else:s+=1
    return c
