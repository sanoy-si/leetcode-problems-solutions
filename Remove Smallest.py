for i in range(int(input())):
    length = int(input())
    nums= [int(i) for i in input().split()]
    nums.sort()
    ans = "YES"
    for i in range(length - 1):
        if abs(nums[i+1] - nums[i]) > 1:
            ans = "NO"
            break
    print(ans)




