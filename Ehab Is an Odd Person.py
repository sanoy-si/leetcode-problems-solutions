ln=int(input())
nums=[int(i) for i in input().split()]
e,v=0,0
for i in nums:
    if i%2==0:v+=1
    else:e+=1
if e and v: print(*list(sorted(nums)))
else:print(*nums)
