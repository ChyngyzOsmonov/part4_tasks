class MoneyFmt:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


    def __str__(self):
        return ('{:,.2f} {}'.format(self.amount,self.currency))
        
money = MoneyFmt(-12345665432, '$')
print(money.__str__())