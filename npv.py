class CashFlow(list):
    def __init__(self, iterable, growth=0):
        self.growth = growth
        self.iterable = map(lambda x: x*(1+self.growth), iterable)
        self.period = len(self.iterable)
        super().__init__(self.iterable)


print(CashFlow([1,2,3], growth=0.02))
c = CashFlow([1,2,3], growth=0.03)
c.append(5)
print(c[:2])