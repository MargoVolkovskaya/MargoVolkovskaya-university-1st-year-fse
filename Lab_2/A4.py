LIMIT = 10000

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# k = 0, если a >= b, и k = -1, если a < b
k = (a - b) // LIMIT
print(a * (k + 1) - b * k)
