class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        p = 0
        to_be_banned_r = 0
        to_be_banned_d = 0

        r = senate.count('R')
        d = senate.count('D')
        senate = list(senate)

        while True:
            ind = p % len(senate)
            if senate[ind] == 'R':
                if to_be_banned_r != 0:
                    senate[ind] = '0' 
                    to_be_banned_r -= 1
                    r -= 1

                else:
                    if d == 0:
                        return "Radiant"
                    to_be_banned_d += 1

            elif senate[ind] == 'D':
                if to_be_banned_d != 0:
                    senate[ind] = '0' 
                    to_be_banned_d -= 1
                    d -= 1

                else:
                    if r == 0:
                        return "Dire"
                    to_be_banned_r += 1
            
            p += 1

