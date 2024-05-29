class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & 1 << i:
                    count += 1
            
            if count % 3 != 0:
                answer = answer | 1 << i
        
        if nums.count(answer) == 1:
            return answer
        
        else:
            ans = []
            
            for i in range(32):
                if answer & 1 << i:
                    ans.append('0')
                
                else:
                    ans.append('1')

            return -(int(''.join(ans[::-1]), 2) + 1)
