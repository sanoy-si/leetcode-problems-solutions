class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            num = list(map(int,list(str(num))))
            num.sort()
            
            seeker = 0
            while seeker < len(num) and num[0] == 0 :
                if num[seeker] != 0:
                    num[seeker], num[0] = num[0], num[seeker]
                    
                seeker += 1

            num = list(map(str, num))

            return int(''.join(num))
        
        else:
            num = list(map(int, str(num)[1:]))
            num.sort(reverse = True)
        
            num = list(map(str, num))

            return -int(''.join(num))




        