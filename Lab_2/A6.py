N = int(input())
hours = N // 3600
N %= 3600
minutes = N // 60
N %= 60
seconds = N
print('{}:{:02}:{:02}'.format(hours, minutes, seconds))