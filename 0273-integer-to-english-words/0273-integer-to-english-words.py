class Solution:
    def numberToWords(self, num: int) -> str:
        smalls = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


        def dfs(num):
            if num < 20:
                return smalls[num]
            
            if num < 100:
                return tens[num // 10] + ('' if num % 10 == 0 else ' ' + smalls[num % 10])
            
            return smalls[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' ' + dfs(num % 100))
        
        answer = []
        billions, num = divmod(num, 1000000000)
        millions, num = divmod(num, 1000000)
        thousands, num = divmod(num, 1000)

        if billions:
            answer.append(dfs(billions) + ' Billion')
        if millions:
            answer.append(dfs(millions) + ' Million')
        if thousands:
            answer.append(dfs(thousands) + ' Thousand')
        if num:
            answer.append(dfs(num))
        
        return ' '.join(answer)
 