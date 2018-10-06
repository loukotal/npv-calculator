class CashFlow:
    # TODO add status - to check if the CF starts from now or the next year
    def __init__(self, cashflow, growth=0):
        self.growth = growth
        self.period = len(cashflow)
        self._original_cf = cashflow
        self.cashflow = list(map(lambda pair: pair[0]*(1+self.growth)**pair[1], zip(cashflow, range(0,self.period))))
        
        # super().__init__(self._original_cf)

    def __repr__(self):
        return "{}".format(self.cashflow)

    def append(self, value):
        self._original_cf.append(value)
        self._set_period(len(self._original_cf))
        self._recalculate_cf()

    def _set_period(self, new_period):
        self.period = new_period

    def set_growth(self, new_growth):
        self.growth = new_growth
        self._recalculate_cf()

    # Recalculate cf after changing the growth or adding a new item to the list.
    def _recalculate_cf(self):
        self.cashflow = list(map(lambda pair: pair[0]*(1+self.growth)**pair[1], zip(self._original_cf, range(0,self.period))))
        # return self.cashflow

    def sum_cashflow(self, ndigits=3):
        return round(sum(self.cashflow), ndigits)


class NetPresentValue(CashFlow):
    def __init__(self, cashflow, growth=0, investment=0, discount=0):
        self.investment = investment
        self.discount = discount
        super().__init__(cashflow, growth)

    def calc_npv(self, ndigits=2):
        return round(sum(map(lambda pair: pair[0]/(1+self.discount)**pair[1], zip(self.cashflow, range(1,self.period+1)))) + self.investment, ndigits)

# print(CashFlow([1,2,3], growth=0.02))
#c = CashFlow([1,2,3], growth=0.03)
#c.append(5)
#print(c)
# print(c._original_cf)

#c.set_growth(0.00)
#print(c.growth)
#print(c.cashflow)
# print(c.calculate_cashflow())
#print(c.sum_cashflow(ndigits=1))
#c.append(6)

npv = NetPresentValue([100,100,100,100,100], investment=-100, discount=0.05)
print(npv.cashflow)
print(npv.calc_npv())