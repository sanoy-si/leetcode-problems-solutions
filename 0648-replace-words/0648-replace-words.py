class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        
        curr.is_end = True

    def find_root_word(self, word: str) -> bool:
        curr = self.root
        root_word = []

        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return word
            
            curr = curr.children[idx]
            root_word.append(chr(ord('a') + idx))

            if curr.is_end:
                return ''.join(root_word)
        
        return word 


    
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        sentence = list(sentence.split())
        for i, word in enumerate(sentence):
            sentence[i] = trie.find_root_word(word)
        
        return ' '.join(sentence)