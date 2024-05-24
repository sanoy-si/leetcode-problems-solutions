class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_counter = Counter(letters)

        def is_valid(word):
            return Counter(word) - letters_counter == Counter()
        
        def get_score(word):
            answer = 0
            for char in word:
                answer += score[ord(char) - ord('a')]
            
            return answer
        
        answer = 0
        def backtrack(idx, current_score):
            nonlocal answer, letters_counter
            if idx == len(words):
                answer = max(answer, current_score)
                return 
            
            backtrack(idx + 1, current_score)

            word = words[idx]
            if is_valid(word):
                word_counter = Counter(word)

                current_score += get_score(word)
                letters_counter -= word_counter
                backtrack(idx + 1, current_score)

                letters_counter += word_counter
        
        backtrack(0, 0)

        return answer