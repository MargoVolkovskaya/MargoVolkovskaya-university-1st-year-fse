import string
def clean_text(text):

    while True:
        position1 = text.rfind('(')
        if position1 == -1:
            break
        position2 = text.find(')',position1)
        if position2 == -1:
            text = text[:position1] + text[position1 + 1:]
            continue
        text = text[:position1] + text[position2 + 1:]

    while "  " in text:
        text = text.replace("  ", " ")

    for mark in string.punctuation:
        text = text.replace(" " + mark, mark)



    return text

def main():
    input_text = input('Введите строку: ')
    result_text = clean_text(input_text)
    print("\nОтвет на задачу:",result_text)


main()



# input
# Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (()).