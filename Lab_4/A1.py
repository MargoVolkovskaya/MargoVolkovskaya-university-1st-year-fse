import random
import time
N = int(input("Введите количество примеров: "))
count_time = 0
count_true = 0
for i in range(N):
    print(f"Вопрос {i + 1}/{N}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    ans = a * b

    start_time = time.time()
    while True:
        try:
            answer = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    time_spend = time.time() - start_time
    count_time += time_spend
    if ans == answer:
        print("Верно!",end="")
        count_true += 1
    else:
        print(f"Неверно! Правильно: {ans}",end="")
    print(f"(Время: {time_spend:.1f} сек)")

print(f"{'=' * 40} \nСТАТИСТИКА: \n{'=' * 40}")
print(f"Общее время: {count_time:.1f} секунд\nСреднее время на вопрос: {count_time / N:.1f} сек")
print(f"Правильных ответов: {count_true}/{N} \nПроцент правильных: {count_true / N * 100:0.01f}%")