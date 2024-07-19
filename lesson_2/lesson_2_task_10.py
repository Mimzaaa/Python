def bank(X, Y):
    interest_rate = 0.10                     # процентная ставка
    deposit_amount = X                       # сумма вклада
    for year in range(Y):                    # расчет суммы вклада для каждого года
       deposit_amount += deposit_amount * interest_rate   # увеличение вклада на 10% каждый год
    return deposit_amount

# Пример использования функции:
initial_deposit = 1000
years = 5
final_amount = bank(initial_deposit, years)
print(f"Сумма на счету после {years} лет: {final_amount} рублей")
