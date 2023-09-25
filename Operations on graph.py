from sys import stdin,stdout
from collections import defaultdict

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


v=intinp()
for i in range(intinp()):
   operation = intlst()
   if operation[0] == 1:
        graph[operation[1]].append(operation[2])
        graph[operation[2]].append(operation[1])
   else:
       if graph[operation[1]]:print(*graph[operation[1]])
