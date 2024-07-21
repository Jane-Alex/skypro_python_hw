from math import ceil

def square(a):
    s = a*a
    return s
   
a = float(input("Введите длину стороны квадрата: "))

result = square(a)

rounded_result = ceil(result)

print(f'Площадь квадрата = {rounded_result}')