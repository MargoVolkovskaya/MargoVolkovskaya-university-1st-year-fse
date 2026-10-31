def draw_rectangle(rows,columns,ch):
    for i in range(rows):
        for j in range(columns):
            print(ch,end="")
        print()


def draw_triangle(rows,ch):
    for i in range(rows):
        for j in range(i + 1):
            print(ch,end="")
        print()


def draw_border(rows,columns,ch):
    for i in range(rows):
        for j in range(columns):
            if i in (0, rows - 1) or j in (0, columns - 1):
                print(ch,end="")
            else:
                print(" ",end="")
        print()


def main():
    n,m = map(int,input("Введите размеры: ").split())
    print("ПРЯМОУГОЛЬНИК:")
    draw_rectangle(n, m, '#')
    print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
    draw_triangle(n, '#')
    print("РАМКА:")
    draw_border(n, m, '#')


main()