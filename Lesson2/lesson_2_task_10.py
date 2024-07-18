def bank(x, y):
    rate = 0.10
    for _ in range(y):
        x += x * rate
    return x

deposit = int(input("Введите сумму вклада в рублях: "))
years = int(input("Укажите срок влада в годах: "))
final_amount = bank(deposit, years)
print(f'Сумма на счету спустя {years} лет: {final_amount} рублей')