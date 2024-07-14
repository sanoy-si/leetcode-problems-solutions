class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def handle_digits(formula):
            new_formula = []
            p = 0
            while p < len(formula):
                if formula[p].isdigit():
                    temp = []
                    while p < len(formula) and formula[p].isdigit():
                        temp.append(formula[p])
                        p += 1
                    
                    new_formula.append(int(''.join(temp)))
                
                else:
                    new_formula.append(formula[p])
                    p += 1
            
            return new_formula

        formula = handle_digits(formula)
        stack = []
        
        for thing in formula:
            if stack and type(stack[-1]) != int and type(thing) != int and thing.upper() == thing and stack[-1] not in '()':
                stack.append(1)

            if type(thing) == int and stack[-1] == ')':
                stack.pop()
                temp = []
                while stack[-1] != '(':
                    if type(stack[-1]) == int:
                        temp.append(stack.pop() * thing)

                    else:
                        temp.append(stack.pop())
                
                stack.pop()
                stack += temp[::-1]

            else:
                stack.append(thing)

        if stack and type(stack[-1]) != int:
            stack.append(1)
        
        print(stack)
        counter = Counter()
        p = 0
        while p < len(stack):
            temp = []
            while type(stack[p]) == str:
                temp.append(stack[p])
                p += 1
            
            counter[''.join(temp)] += stack[p]
            p += 1


        formula = ''.join(sorted([element + str(count) if count > 1 else element for element, count in counter.items()]))
        return formula
                

 