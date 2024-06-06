class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        seeker = place_holder = 0
        count = 0

        while seeker < len(s):
            if s[seeker] == '0':
                count += seeker - place_holder

                s[seeker], s[place_holder] = s[place_holder], s[seeker]
                
                place_holder += 1

            seeker += 1
        
        return count

        