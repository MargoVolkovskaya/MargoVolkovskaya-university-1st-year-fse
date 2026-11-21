import re

def split_sentences(text):
    return re.split(r"\t", text.strip())


def open_file(name):
    answer = []
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            answer.append(split_sentences(line))
    return answer


def answer_for_search(index,operation,input_data,f):
    print(f"{index + 1:03d}", operation[0], operation[1], file=f)
    print(f"{"organism":<33} {"protein"}",file=f)
    value = operation[1]
    flag = False
    for a in input_data:
       if value in a[2]:
           flag = True
           print(f"{a[1]:<33} {a[0]}",file=f)
    if flag == False:
        print("NOT FOUND",file=f)
    print('-' * 40, file=f)


def answer_for_diff(index,operation,input_data,f):
    print(f"{index + 1:03d}", operation[0], operation[1],operation[2], file=f)
    print("amino-acides difference:", file=f)
    pos1,pos2 = -1,-1
    for index in range(len(input_data)):
        temp = input_data[index][0]
        if temp == operation[1]:
            pos1 = index
        elif temp == operation[2]:
            pos2 = index
    if pos1 == -1 or pos2 == -1:
        print("MISSING:",(operation[1] if pos1 == -1 else ""),(operation[2] if pos2 == -1 else ""),file=f)
    else:
        len1 = len(input_data[pos1][2])
        len2 = len(input_data[pos2][2])
        diff_count = abs(len1 - len2)
        for index in range(min(len1,len2)):
            if input_data[pos1][2][index] != input_data[pos2][2][index]:
                diff_count += 1
        print(diff_count, file=f)
    print('-' * 40, file=f)


def answer_for_mode(index,operation,input_data,f):
    print(f"{index + 1:03d}", operation[0], operation[1], file=f)
    print("amino-acid occurs:", file=f)
    pos = -1
    for index in range(len(input_data)):
        temp = input_data[index][0]
        if temp == operation[1]:
            pos = index
    if pos == -1:
        print("MISSING:",operation[1],file=f)
    else:

        letters = dict()
        maximal = 0
        char = 'a'
        for letter in input_data[pos][2]:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

            if letters[letter] > maximal:
                maximal = letters[letter]
                char = letter
            elif letters[letter] == maximal:
                char = min(char, letter)
        print(f"{char:<33} {maximal}", file=f)
    print('-' * 40, file=f)

def genedata(input_data,input_operations):
    with open("genedata.txt", "w", encoding="utf-8") as f:
        print("Margarita Volkovskaya", "Genetic Searching", '-' * 40, sep ="\n", file=f)

        for index in range(len(input_operations)):
            operation = input_operations[index]
            kind = operation[0]
            if kind == "search":
                answer_for_search(index,operation,input_data,f)
            elif kind == "diff":
                answer_for_diff(index,operation,input_data,f)
            else:
                answer_for_mode(index,operation,input_data,f)


def main():
    input_data = open_file('sequences.0.txt')
    input_operations = open_file('commands.0.txt')
    genedata(input_data,input_operations)


main()