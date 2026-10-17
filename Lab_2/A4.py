a = int(input())
b = int(input())
k = (a - b) // 10000
ans = a * (k + 1) - b * k
print(ans)