salary=20000
spend=30000
money_capital=spend-salary
increase=0.03
for i in range(2,10):
    spend*=(1+increase)
    money_capital += spend - salary
print(round(money_capital,2))