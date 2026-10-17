import string
password = input()
length = len(password)
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
special_symbol = '*-#'
upper = password.upper()
lower = password.lower()
flag = 0
if length != 8:
    flag = 1
    print("Длина пароля не равна 8")
if password == lower:
    flag = 1
    print("В пароле отсутствуют заглавные буквы")
if password == upper:
    flag = 1
    print("В пароле отсутствуют строчные буквы")
if not(any(symbol.isdigit() for symbol in password)):
    flag = 1
    print("В пароле отсутствуют цифры")
if not(any(symbol in special_symbol for symbol in password)):
    flag = 1
    print("В пароле отсутствуют специальные символы")
if not(all(symbol in allowed for symbol in password)):
    flag = 1
    print("В пароле используются непредусмотренные символы")

if flag == 0:
    print("Надежный пароль")