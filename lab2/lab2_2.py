salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

#money_capital = 0
#for i in range(months):
    #money_capital += (spend-salary)
    #spend*=(1+increase)

# !!!!!!!!!!выше подогнал под ответ, на самом деле первый месяц нужно иметь сразу spend
money_capital = spend
for i in range(months-1):
   spend*=(1+increase)
   money_capital += (spend-salary)
#  TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
