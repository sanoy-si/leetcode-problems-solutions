class Solution:
    def isValid(self, s: str) -> bool:
        nl=[]
        for i in s:
            if nl:
                if (nl[-1]=='('and i==')') or (nl[-1]=='['and i==']') or (nl[-1]=='{'and i=='}'):
                    nl.pop()
                else:nl.append(i)
            else:nl.append(i)
        if nl:return False
        return True
