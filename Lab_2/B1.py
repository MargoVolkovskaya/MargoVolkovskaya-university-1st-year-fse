n,m = input().split()
n = int(n)
m = round(float(m),2)
a = []
for i in range(n):
  a.append(float(input()))
ans = 0.0
print("Margarita")
print("Simple Map Distance Computations")
print(" ")
print("Map Scale Fator:   ",m," miles per inch")
print("      Map      Mileage")
print("      Measure  Distance")
print("=" * 40)
for i in range(n):
  x = round(a[i] * m,1)
  print("# ",i + 1," ",a[i],"  ",x)
  ans += x
print("=" * 40)
print("Total Distance: ",ans,"miles")