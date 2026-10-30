x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if not(x1 // x2 >= 0 and y1 // y2 >= 0):
    print("No")
else:
    print("Yes,",end="")
    if (x1 > 0 and y1 > 0):
        print("I")
    elif (x1 < 0 and y1 > 0):
        print("II")
    elif (x1 < 0 and y1 < 0):
        print("III")
    else:
        print("IV")
