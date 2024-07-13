class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        positions_healths_directions = list(zip(positions, healths, directions))
        positions_healths_directions.sort()
        healths_dict = {}
        stack = []

        for i in range(len(positions)):
            curr_position, curr_health, curr_direction = positions_healths_directions[i]
            should_append = True
            
            while stack and stack[-1][2] == 'R' and curr_direction == 'L':
                former_position, former_health, former_direction = stack.pop()
                
                if former_health > curr_health:
                    former_health -= 1
                    healths_dict[former_position] = former_health
                    stack.append((former_position, former_health, former_direction))
                    should_append = False
                    break
                
                elif former_health == curr_health:
                    healths_dict.pop(former_position)
                    should_append = False
                    break

                else:
                    healths_dict.pop(former_position)
                    curr_health -= 1
                    should_append = True                

            if should_append:
                stack.append((curr_position, curr_health, curr_direction))
                healths_dict[curr_position] = curr_health

        answer = []
        for position in positions:
            if position in healths_dict:
                answer.append(healths_dict[position])
        
        return answer

                
        
       