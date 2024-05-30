class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        
        curr.is_end = True
        print(curr.is_end)


    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node and node.is_end

            if word[i] == '.':
                for j in range(26):
                    if node.children[j]:
                        if dfs(i + 1, node.children[j]):
                            return True
                
                return False
            
            else:
                idx = ord(word[i]) - ord('a')
                
                if not node.children[idx]:
                    return False
                
                return dfs(i + 1, node.children[idx])
                    

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)