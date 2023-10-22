def fun(nums,first):
 
    if first:
        i = 0
    else:
        i = 0
        tof = False if nums[0] > 0 else True
        while i < len(nums) and tof != nums[i] > 0:
            i+=1
    try:
        last = nums[i]
    except:
        return []
    s = [nums[i]]
    i+=1
 
    while i < len(nums):
        # print(i,s)
        if last > 0:
            if nums[i] > 0:
                if s:
                    cma = s.pop()
                    s.append(max(cma,nums[i]))
                else:
                    s.append(nums[i])
            else:
                s.append(nums[i])
        else:
            if nums[i] < 0:
                if s:
                    cma = s.pop()
                    s.append(max(cma,nums[i]))
                else:
                    s.append(nums[i])
            else:
                s.append(nums[i])
        i+=1
        last = s[-1]
 
    return s
 
 
for _ in range(int(input())):
    n = int(input())
    nums = [int(i) for i in input().split()]
    s1 = fun(nums,True)
    s2 = fun(nums,False)
 
    if len(s1) == len(s2):
        print(max(sum(s1),sum(s2)))
    else:
        print(sum(max(s1,s2,key=lambda x:len(x))))
 
 
 
