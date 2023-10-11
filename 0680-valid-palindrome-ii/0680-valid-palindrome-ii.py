class Solution:
    def validPalindrome(self, s: str) -> bool:
        c=0
        s = list(s)
        def colliding(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return (left,right)
                left += 1
                right -= 1
            return True

        ans = colliding(s)
        if ans == True:
            return True
        ans1 = colliding(s[:ans[0]] + s[ans[0]+1:])
        ans2 = colliding(s[:ans[1]] + s[ans[1] + 1 :])

        if True in (ans1,ans2):
            return True
        return False
        

        
        