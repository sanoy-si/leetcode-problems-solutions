class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words = list(map(Counter, words))
        answer = []

        for char in words[0]:
            not_found = False
            while not not_found:
                for word in words:
                    if word[char] > 0:
                        word[char] -= 1
                    
                    else:
                        not_found = True

                if not not_found:
                    answer.append(char)
            
            if not not_found:
                answer.append(char)
        
        return answer