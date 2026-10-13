line_number = 0
distance = -1
distance_c = 0
distance_m = 0
x_c = -1
x_m = -1
y_c = -1
y_m = -1

    with open('1ChaseData.txt','r') as file:
        for line in file:
            line_number += 1

        if line_number == 1:
            n,m = map(int,line.split())
        else:
            parts = line.strip().split()
            wd = parts[0]
            x = parts[1]
            y = parts[2]

            if wd == 'M':
                distance_m += abs(x) + abs(y)
                if x_m == -1 and y_m == -1:
                    x_m = x
                    y_m = y
                else:
                    if x <= 0:
                        if x_m - x > 0:
                            x_m -= x
                        else:
                            x_m = (9 - (abs(x) - x_m))
                    if y <= 0:
                        if y_m - y > 0:
                            y_m -= y
                        else:
                            y_m = (9 - (abs(y) - y_m))
            elif wd == 'C':
                distance_c += abs(x) + abs(y)
                if x_c == -1 and y_c == -1:
                    x_c = x
                    y_c = y
                else:
                    if x <= 0:
                        if x_c - x > 0:
                            x_c -= x
                        else:
                            x_c = (9 - (abs(x) - x_c))
                    if y <= 0:
                        if y_c - y > 0:
                            y_c -= y
                        else:
                            y_c = (9 - (abs(y) - y_c))
            else:
                print(x_c,y_c,x_m,y_m,distance);



