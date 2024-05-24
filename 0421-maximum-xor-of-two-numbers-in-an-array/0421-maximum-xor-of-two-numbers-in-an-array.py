class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            idx = int(char)

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]
        
        curr.is_end = True
    
    def max_xor(self, word):
        curr_idx = 31
        answer = 0
        curr_trie = self.root

        for char in word:
            fav_idx = 0 if int(char) else 1

            if curr_trie.children[fav_idx]:
                answer += 1<<curr_idx
                curr_trie = curr_trie.children[fav_idx]
            
            else:
                curr_trie = curr_trie.children[0 if fav_idx else 1]
            
            curr_idx -= 1
        
        return answer
             

class Solution:
    def findMaximumXOR(self, nums):
        trie = Trie()
        bits = []
        for num in nums:
            bit = bin(num)[2:]
            bits.append(((32 - len(bit)) * '0') + bit)
            trie.insert(bits[-1])

        answer = 0
        for bit in bits:
            answer = max(answer, trie.max_xor(bit))

        return answer