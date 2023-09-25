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

val = 0
for i in range(intinp()):
    row = input()
    val += row.count('1')  
print(val//2)
