class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.children[char]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            current = current.children.get(char)
            if current == None:
                return False
        
        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            current = current.children.get(char)
            if current == None:
                return False
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)