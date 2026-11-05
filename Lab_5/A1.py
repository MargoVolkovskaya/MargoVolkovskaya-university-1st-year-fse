def remove_brackets(text):
    while True:
        position1 = text.rfind('(')
        if position1 == -1:
            break
        position2 = text.find(')',position1)
        if position2 == -1:
            text = text[:position1] + text[position1 + 1:]
        else:
            text = text[:position1] + text[position2 + 1:]

    return text


def remove_spaces(text):
    while "  " in text:
        text = text.replace("  ", " ")

    for mark in ".,?!:;":
        text = text.replace(" " + mark, mark)

    return text.strip()


def shorten_text(text):
    return remove_spaces(remove_brackets(text))


def main():
    input_text = input('Исходный текст: ')
    print("Укороченный текст:", shorten_text(input_text))


main()


# input
# Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (()).