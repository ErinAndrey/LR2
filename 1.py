money_capital=300000
salary=20000
spend=30000
increase=0.05
month=1
money_capital-=spend-salary
while money_capital>0:
    money_capital-=(spend*(1+increase)-salary)
    month+=1
print(month)