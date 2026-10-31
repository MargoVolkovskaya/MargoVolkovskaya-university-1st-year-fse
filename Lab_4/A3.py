def main():
    packets = input("Введите последовательность: ")

    length = len(packets)
    count_zero = packets.count("0")
    count_max_length_zero = 0
    temp = 0
    for i in range(length):
        if packets[i] == "0":
            temp += 1
        else:
            count_max_length_zero = max(count_max_length_zero,temp)
            temp = 0
    count_max_length_zero = max(count_max_length_zero, temp)
    percent = count_zero / length * 100

    if not all(char in '01' for char in packets):
        print("Неверный ввод. Используйте только символы '0' и '1'!")
        return 0
    if length < 5:
        print("Неверный ввод. Длина строки меньше 5")
        return 0

    print(f"Общее количество пакетов: {length}")
    print(f"Количество потерянных пакетов: {count_zero}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {count_max_length_zero}")
    print(f"Процент потерь: {percent:.1f}")
    print(f"Качество связи: ",end="")
    if percent <= 1.0:
        print("отличное качество")
    elif percent <= 5.0:
        print("хорошее качество")
    elif percent <= 10.0:
        print("удовлетворительное качество")
    elif percent <= 20.0:
        print("плохое качество")
    else:
        print("критическое состояние сети")
    return 0

main()