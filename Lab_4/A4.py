def is_valid_format(card_number):
    return (
            card_number.isascii()  # потому что isdigit() считает не только цифры 0 .. 9,но и символы очень похожие на них
            and card_number.isdigit()
            and len(card_number) in (13, 15, 16)
    )


def get_checksum(card_number):
    total = 0
    # изначальный код работал только для чет длины
    # в цикле for i in reversed(range(1, len(cardNumber) + 1, 2)) мог быть выход за границы

    for position, char in enumerate(reversed(card_number)):
        digit = int(char)
        if position % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total


def is_valid_checksum(checksum):
    return checksum % 10 == 0


def get_card_type(card_number):
    length = len(card_number)
    prefix = card_number[:2]
    # неверный приоритет был
    if length in (13, 16) and card_number.startswith("4"):
        return "Visa"
    if length == 15 and prefix in ("34", "37"):
        return "American Express"
    if length == 16 and prefix in ("51", "52", "53", "54", "55"):
        return "MasterCard"
    return None


def main():
    card_number = input("Enter Card Number: ")

    if not is_valid_format(card_number):
        print("Wrong Input. Try again...")
        return

    card_type = get_card_type(card_number)
    # первоначальная проверка is_valid_checksum могла просто завершить прграмму ничего не выдав
    # суммы могли сойтись, а тип нет, поэтому Valid и None.
    if card_type is not None and is_valid_checksum(get_checksum(card_number)):
        print("Valid")
        print(card_type)
    else:
        print("Invalid")  # был неверный отступ


main()