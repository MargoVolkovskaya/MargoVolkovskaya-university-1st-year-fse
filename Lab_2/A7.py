x1 = int(input("Введите координату первой клетки по оси ОХ: "))
y1 = int(input("Введите координату первой клетки по оси ОУ: "))
x2 = int(input("Введите координату клетки по оси ОХ: "))
y2 = int(input("Введите координату клетки по оси ОУ: "))

color1 = (x1 + y1) % 2
color2 = (x2 + y2) % 2

if color1 == color2:
    print("YES")
    print("White" if color1 == 0 else "Black")
else:
    print("NO")