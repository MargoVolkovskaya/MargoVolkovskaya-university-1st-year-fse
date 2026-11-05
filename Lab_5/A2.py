import re


def split_sentences(text):
    return re.split(r"(?<=[.?!])\s+", text.strip())


def main():
    text = input("Введите текст: ")
    sentences = split_sentences(text)

    for sentence in sentences:
        print(sentence)
    count = len(sentences)
    print("Предложений в тексте:",count)


main()

# input
# He jests at scars.     That never felt a wound! Hello, friend!       Are you OK?