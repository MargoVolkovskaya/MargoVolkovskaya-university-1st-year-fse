def split_sentences(text):
    return text.split()


def abbreviation(text):
    words =  split_sentences(text)
    answer = ""

    for word in words:
        if len(word) < 3:
            continue
        answer += word[0]

    return answer.upper()


def main():
    input_text = input("Введите текст: ")
    print(abbreviation(input_text))

main()