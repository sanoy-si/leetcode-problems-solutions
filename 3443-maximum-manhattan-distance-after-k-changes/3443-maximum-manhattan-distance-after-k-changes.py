class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        curr_n_count = curr_s_count = curr_w_count = curr_e_count = 0
        answer = 0
        for char in s:
            if char == "N":
                curr_n_count += 1
            
            elif char == "E":
                curr_e_count += 1
            
            elif char == "S":
                curr_s_count += 1
            
            else:
                curr_w_count += 1

            max_change = min(curr_e_count, curr_w_count) + min(curr_n_count, curr_s_count)
            unchanged = abs(curr_e_count - curr_w_count) + abs(curr_n_count - curr_s_count)
            answer = max(answer, unchanged + 2 * min(k, max_change))
        
        return answer