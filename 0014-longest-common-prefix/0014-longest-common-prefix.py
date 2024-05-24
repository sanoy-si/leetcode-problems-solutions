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

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            
            if not curr.children[idx]:
                return False
            
            curr = curr.children[idx]
        
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            idx = ord(char) - ord('a')
            
            if not curr.children[idx]:
                return False
        
            curr = curr.children[idx]
        
        return True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        trie = Trie()

        for word in strs:
            trie.insert(word)
        
        answer = []
        stack = [trie.root]
        while stack:
            node = stack.pop()
            count = 0
            idx = 0
            for i in range(26):
                if node.children[i]:
                    count += 1
                    idx = i

            if count != 1:
                break
            
            stack.append(node.children[idx])
            answer.append(chr(97 + idx))

        min_length = len(min(strs, key = lambda x: len(x)))

        if answer:
            return ''.join(answer[:min(len(answer), min_length)])

        return ''

        