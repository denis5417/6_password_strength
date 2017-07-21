import sys
import string


def check_black_list(password):
    black_list = open("10k_most_common.txt").read().split("\n")
    if password in black_list:
        print("Ваш пароль в черном списке")
        print("Ваша оценка 0 из 10")
        sys.exit()
    for bad_pass in black_list:
        if bad_pass in password:
            print("Пароль {} из черного списка является подстрокой вашего пароля 1 балл".format(bad_pass))
            return 1
        if password in bad_pass:
            print("Пароль является построкой пароля {} из черного списка. 1 балл".format(bad_pass))
            return 1
    print("Пароля нет в черном списке. 2 балла")
    return 2


def check_case(password):
    if password.upper() != password and password.lower()!= password:
        print("В пароле используются заглавные и строчные буквы одновременно. 2 балла")
        return 2
    else:
        print("В пароле не используются заглавные и строчные буквы одновременно. 0 баллов")
        return 0


def check_special_characters(password):
    for char in string.punctuation:
        if char in password:
            print("В пароле используются специальные символы. 2 балла")
            return 2
    print("В пароле не используются специальные символы. 0 балов")
    return 0


def check_len(password):
    if len(password) < 12:
        print("В пароле меньше 12 символов. 0 баллов")
        return 0
    elif 12 <= len(password) <= 14:
        print("В пароле от 12 до 14 символов. 1 балл")
        return 1
    else:
        print("В пароле больше 14 символов. 2 балла")
        return 2


def check_dates(password):
    for year in range(1900, 2100):
        if str(year) in password:
            print("В пароле есть дата. 0 баллов")
            return 0
    print("В пароле нет даты. 2 балла")
    return 2

if __name__ == '__main__':
    if len(sys.argv) > 1:
        password = sys.argv[1]
        points = 0
        points += check_black_list(password)
        points += check_case(password)
        points += check_special_characters(password)
        points += check_len(password)
        points += check_dates(password)
        print("Ваша оценка – {} из 10".format(points))
    else:
        print("Вы не ввели пароль")