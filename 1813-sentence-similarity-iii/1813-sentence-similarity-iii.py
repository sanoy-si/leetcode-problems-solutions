class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        while sentence1 and sentence2 and sentence1[-1] == sentence2[-1]:
            sentence1.pop()
            sentence2.pop()
        
        sentence1 = sentence1[::-1]
        sentence2 = sentence2[::-1]

        while sentence1 and sentence2 and sentence1[-1] == sentence2[-1]:
            sentence1.pop()
            sentence2.pop()
        

        return not sentence1 or not sentence2
