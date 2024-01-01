class ATM:

    def __init__(self):
        self.moneys = [20,50,100,200,500]
        self.balance = defaultdict(int)

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.balance[self.moneys[i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        p = len(self.moneys) - 1
        cash = [0, 0, 0, 0, 0]
        while p >= 0 and amount > 0:
            print(self.balance,amount)

            if self.balance[self.moneys[p]] == 0:
                    p -= 1
                    continue
                    
            used_note = min(self.balance[self.moneys[p]], amount // self.moneys[p])
            cash[p] += used_note
            self.balance[self.moneys[p]] -= used_note
            amount -= self.moneys[p] * used_note

            p -= 1
        

        if amount != 0:
            for i in range(len(cash)):
                self.balance[self.moneys[i]] += cash[i]
            return [-1]

        return cash



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)