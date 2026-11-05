def get_used(previous, current):
    if current < previous:
        return current + (10000 - previous)
    return current - previous


def get_price(used):
    if used == 0:
        return 0
    if used <= 300:
        return 21
    if used <= 600:
        return 21 + 0.06 * (used - 300)
    if used <= 800:
        return 21 + 0.06 * 300 + 0.04 * (used - 600)
    return 21 + 0.06 * 300 + 0.04 * 200 + 0.025 * (used - 800)


def main():
    previous = int(input("Введите предыдущее показание:"))
    current = int(input("Введите текущее показание:"))

    used = get_used(previous, current)
    price = get_price(used)

    if used > 0:
        price_average = price / used
    else:
        price_average = 0

    print(f"{'Предыдущее':<15} {'Текущее':<15} {'Использовано':<15} {'К оплате':<15} {'Ср. цена м³':<15}")
    print(f"{previous:<15} {current:<15} {used:<15} {price + 0.001:<15.2f} {price_average:<15.2f}")


main()