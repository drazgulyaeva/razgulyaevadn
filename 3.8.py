money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
cur_money = money_capital - spend + salary

while cur_money > 0:
    month = month + 1
    cur_money = cur_money + salary - spend * (1.05 ** month)
# TODO Оформить решение

print(month)
