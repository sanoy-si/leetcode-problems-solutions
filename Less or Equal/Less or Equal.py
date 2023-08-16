length, k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
nums.sort()
if k==0:
    if nums[0]<=1:print(-1)
    else:print(nums[0]-1)
else:
    if k!=length and nums[k] == nums[k - 1]:print(-1)
    else:print(nums[k-1])
