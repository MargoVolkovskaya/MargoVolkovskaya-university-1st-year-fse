import random
import time

MIN_FACTOR = 2
MAX_FACTOR = 9
LINE = "=" * 40


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число!")


def ask_question():
    a = random.randint(MIN_FACTOR, MAX_FACTOR)
    b = random.randint(MIN_FACTOR, MAX_FACTOR)

    start = time.time()
    user_answer = read_int(f"{a} × {b} = ")
    elapsed = time.time() - start

    is_correct = (user_answer == a * b)
    if is_correct:
        print(f"Верно! (Время: {elapsed:.1f} сек)")
    else:
        print(f"Неверно! Правильно: {a * b} (Время: {elapsed:.1f} сек)")
    return is_correct, elapsed


def print_statistics(total_time, correct, n):
    print(LINE)
    print("СТАТИСТИКА:")
    print(LINE)
    print(f"Общее время: {total_time:.1f} секунд")
    print(f"Среднее время на вопрос: {total_time / n:.1f} сек")
    print(f"Правильных ответов: {correct}")
    print(f"Процент правильных: {correct / n * 100:.1f}%")


def main():
    n = read_int("Введите количество примеров: ")
    total_time = 0.0
    correct = 0

    for i in range(1, n + 1):
        print(f"Вопрос {i}/{n}")
        is_correct, elapsed = ask_question()
        total_time += elapsed
        correct += is_correct

    print_statistics(total_time, correct, n)


main()