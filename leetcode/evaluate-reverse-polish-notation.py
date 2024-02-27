class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()

                val = eval(num1 + token + num2)

                if val < 0:
                    val = ceil(val)

                else:
                    val = floor(val)

                stack.append(str(val))
            
            else:
                stack.append(token)
        
        return int(stack.pop())