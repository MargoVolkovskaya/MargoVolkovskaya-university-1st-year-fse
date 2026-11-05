def quarter(x, y):
    if x > 0 and y > 0:
        return "I"
    if x < 0 and y > 0:
        return "II"
    if x < 0 and y < 0:
        return "III"
    return "IV"


def main():
    x1 = int(input("Введите кординату первой точки по оси ОХ:"))
    y1 = int(input("Введите кординату первой точки по оси ОУ:"))
    x2 = int(input("Введите кординату первой точки по оси ОХ:"))
    y2 = int(input("Введите кординату первой точки по оси ОУ:"))

    quarter1 = quarter(x1, y1)
    quarter2 = quarter(x2, y2)

    if quarter1 == quarter2:
        print("Yes,", quarter1)
    else:
        print("No")


main()