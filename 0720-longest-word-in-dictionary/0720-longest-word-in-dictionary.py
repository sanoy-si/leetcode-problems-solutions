class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


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


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        answer = ''
        def dfs(node, word):
            nonlocal answer
            for i, child in enumerate(node.children):
                if child and child.is_end:
                    word.append(chr(97 + i))
                    dfs(child, word[:])
                    word.pop()
                
                else:
                    if len(answer) < len(word):
                        answer = word 
                    
        
        dfs(trie.root, [])

        return ''.join(answer)




        