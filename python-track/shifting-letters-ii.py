class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        chng_list = [0 for char in s]
        
        for left, right, dirn in shifts:
            k = 1 if dirn else -1
           
            chng_list[left] += k
            
            if right + 1 < len(chng_list):
                chng_list[right + 1] -= k
        
        
        chng_list_psum = []
        running_sum = 0

        for aski in chng_list:
            running_sum += aski
            chng_list_psum.append(running_sum)
        

        chars = [chr((ord(s[i]) + chng_list_psum[i] - 97 + 26) % 26 + 97) for i in range(len(s))]

        return ''.join(chars)
        