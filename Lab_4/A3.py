def quality(percent):
    if percent <= 1:
        return "отличное качество"
    if percent <= 5:
        return "хорошее качество"
    if percent <= 10:
        return "удовлетворительное качество"
    if percent <= 20:
        return "плохое качество"
    return "критическое состояние сети"


def main():
    packets = input("Введите последовательность: ")

    if not all(char in '01' for char in packets):
        print("Неверный ввод. Используйте только символы '0' и '1'!")
        return
    if len(packets) < 5:
        print("Неверный ввод. Длина строки меньше 5")
        return

    total = len(packets)
    lost = packets.count("0")
    percent = lost / total * 100
    longest_zero = max(len(part) for part in packets.split("1"))

    print(f"Общее количество пакетов: {total}")
    print(f"Количество потерянных пакетов: {lost}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {longest_zero}")
    print(f"Процент потерь: {percent:.1f}")
    print(f"Качество связи: {quality(percent)}")


main()