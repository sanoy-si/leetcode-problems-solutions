from sys import stdin,stdout
from collections import defaultdict
input = stdin.readline
def intinp():
    return int(stdin.readline())
def intlst():
    return list(map(int,stdin.readline().strip().split()))
def strlst():
    s=stdin.readline().strip()
    return list(s[:len(s)])
def intitr():
    return map(int,stdin.readline().strip().split())
def inpsplt(by = ' '):
    return stdin.readline().strip().split(by)

graph = defaultdict(list)
for i in range(intinp()):
    row = intlst()
    for j,k in enumerate(row):
        if k == 1:graph[i].append(j+1) 
for i,j in graph.items():
    print(len(j),*list(sorted(j)))
