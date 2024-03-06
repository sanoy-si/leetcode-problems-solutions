class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.combs = []

        def dfs(comb, openning, closing):
            if openning == closing == 0:
                self.combs.append(''.join(comb[:]))
                return
            
            if openning > 0:
                comb.append("(")
                dfs(comb[:], openning - 1, closing)
                comb.pop()

            if openning != closing:
                comb.append(")")
                dfs(comb[:], openning, closing - 1)
        
        dfs([], n, n)

        return self.combs

