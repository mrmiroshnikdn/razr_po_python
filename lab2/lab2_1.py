money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
i=0
while int(money_capital) >= salary:
    money_capital=money_capital-spend*(1+i*increase)+salary
    i+=1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
print("Количество месяцев, которое можно протянуть без долгов:",i)