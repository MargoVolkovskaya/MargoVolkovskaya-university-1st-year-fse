def draw_rectangle(rows,columns,ch):
    for i in range (rows):
        for j in range (columns):
            print(ch,end="")
        print()

def draw_triangle(rows,ch):
    for i in range (rows):
        for j in range (i + 1):
            print(ch,end="")
        print()

def draw_border(rows,columns,ch):
    for i in range (rows):
        for j in range (columns):
            if j == 0 or j == columns - 1:
                print(ch,end="")
            elif i == 0 or i == rows - 1:
                print(ch,end="")
            else:
                print(" ",end="")
        print()

n,m = map(int,input("Введите размеры: ").split())
draw_rectangle(n,m,'#')
draw_triangle(n,'#')
draw_border(n,m,'#')
