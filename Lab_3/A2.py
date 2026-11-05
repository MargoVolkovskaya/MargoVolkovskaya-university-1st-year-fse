import string

SPECIAL = "*-#"
ALLOWED = string.ascii_letters + string.digits + SPECIAL


def check_password(password):
    errors = []
    if len(password) != 8:
        errors.append("Длина пароля не равна 8")
    if not any(c in string.ascii_uppercase for c in password):
        errors.append("В пароле отсутствуют заглавные буквы")
    if not any(c in string.ascii_lowercase for c in password):
        errors.append("В пароле отсутствуют строчные буквы")
    if not any(c in string.digits for c in password):
        errors.append("В пароле отсутствуют цифры")
    if not any(c in SPECIAL for c in password):
        errors.append("В пароле отсутствуют специальные символы")
    if not all(c in ALLOWED for c in password):
        errors.append("В пароле используются непредусмотренные символы")
    return errors


def main():
    password = input("Введите пароль для проверки:")
    errors = check_password(password)

    if errors:
        for error in errors:
            print(error)
    else:
        print("Надежный пароль")


main()