class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tot_skill = skill[0] + skill[-1]
        che = skill[0] * skill[-1]

        left = 1
        right = len(skill) - 2
        while left < right:
            if skill[left] + skill[right] != tot_skill:
                return -1
            che += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return che

        
        