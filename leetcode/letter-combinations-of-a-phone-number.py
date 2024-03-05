class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        self.combination = []

        def dfs(ind, current):
            if ind == len(digits):
                if current:
                    self.combination.append(''.join(current[:]))
                return

            for char in self.map[digits[ind]]:
                current.append(char)
                dfs(ind + 1, current)
                current.pop()

        dfs(0, [])

        return self.combination
