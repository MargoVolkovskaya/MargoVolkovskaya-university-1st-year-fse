previous = int(input())
current = int(input())
if current < previous:
    used = current + (10000 - previous)
else:
    used = (current - previous)
if used <= 300:
    price = 21
elif used <= 600:
    price = 21 + 0.06 * (used - 300)
elif used <= 800:
    price = 21 + 0.06 * 300 + 0.04 * (used - 600)
else:
    price = 21 + 0.06 * 300 + 0.04 * 200 + 0.025 * (used - 800)
price_average = price / used
print(f"{'Предыдущее' :<15} {'Текущее' :<15} {'Использовано' :<15} {'К оплате' :<15} {'Ср. цена m^3' :<15}")
print(f"{previous :<15} {current :<15} {used :<15} {(price + 0.001) :<15.2f} {(price_average + 0.001) :<15.2f}")
