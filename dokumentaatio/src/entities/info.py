class Info:
    def __init__(self, amount, date, inorout, planned):
        "amount tells the sum of the transfer"
        "date tells the date of the transaction"
        "inorout is an integer: 0 for income, 1 for outcome"
        "planned is an integer: 0 for planned, 1 for happened"
        self.amount = amount
        self.date = date
        self.inorout = inorout
        self.planned = planned