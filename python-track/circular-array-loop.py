class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def cycle(i:int, nums):
            slow = fast = i
            while True:
                fast = (fast + nums[fast]) % len(nums)
                if fast < 0:
                    fast = -(abs(fast)) % len(nums)
                    fast = len(nums) + fast 

                fast = (fast + nums[fast]) % len(nums) 
                if fast < 0:
                    fast = -(abs(fast)) % len(nums)
                    fast = len(nums) + fast 

                slow = (slow + nums[slow]) % len(nums)
                if slow < 0:
                    slow = -(abs(slow)) % len(nums)
                    slow = len(nums) + slow  
                
                if fast == slow:
                    break
 
            slow2 = i
            while slow2 != slow:
                slow = (slow + nums[slow]) % len(nums)
                if slow2 < 0:
                    slow2 = -(abs(slow2)) % len(nums)
                    slow2 = len(nums) + slow2  
                slow2 = (slow2 + nums[slow2]) % len(nums)
                if slow2 < 0:
                    slow2 = -(abs(slow2)) % len(nums)
                    slow2 = len(nums) + slow2  
    
            length_count = 1
            slow2 = (slow2 + nums[slow2]) % len(nums)
            if slow2 < 0:
                    slow2 = -(abs(slow2)) % len(nums)
                    slow2 = len(nums) + slow2  
            while slow != slow2:
                if (nums[slow2] < 0 and nums[slow] > 0) or (nums[slow2] > 0 and nums[slow] < 0):
                    return False
                slow2 = (slow2 + nums[slow2]) % len(nums)
                if slow2 < 0:
                    slow2 = -(abs(slow2)) % len(nums)
                    slow2 = len(nums) + slow2  

                length_count += 1
            
            return length_count > 1



        for i in range(len(nums)):
            if cycle(i, nums):
                return True
        
        return False
        