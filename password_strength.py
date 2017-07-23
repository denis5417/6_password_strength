import sys
import string
import os

MAX_POINT = 2
MID_POINT = 1
MIN_POINT = 0


def check_black_list(black_list):
    if password in black_list:
        return None
    for bad_pass in black_list:
        if bad_pass in password:
            return MID_POINT
        if password in bad_pass:
            return MemoryError
    return MAX_POINT


def check_case(password):
    if password.upper() != password and password.lower()!= password:
        return MAX_POINT
    else:
        return MIN_POINT


def check_special_characters(password):
    for char in string.punctuation:
        if char in password:
            return MAX_POINT
    return MIN_POINT


def check_len(password):
    min_len = 12
    good_len = 14
    if len(password) < min_len:
        return MIN_POINT
    elif min_len <= len(password) <= good_len:
        return MID_POINT
    else:
        return MAX_POINT


def check_dates(password):
    min_restricted_num = 1900
    max_restricted_num = 2000
    for year in range(min_restricted_num, max_restricted_num):
        if str(year) in password:
            return MIN_POINT
    return MAX_POINT


def load_black_list(filepath):
    with open(filepath) as black_list_file:
        black_list = black_list_file.read().strip().split()
    return black_list


def check_filepath(filepath):
    return os.path.exists(filepath)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        password = sys.argv[1]
        filepath = sys.argv[2]
        if not check_filepath(filepath):
            print("Файл не существует")
        else:
            points = 0
            check_black_list = check_black_list(load_black_list(filepath))
            if not check_black_list:
                print("Ваша оценка 0 из 10")
            else:
                points += check_black_list
                points += check_case(password)
                points += check_special_characters(password)
                points += check_len(password)
                points += check_dates(password)
                print("Ваша оценка – {} из 10".format(points))
    else:
        print("Вы не ввели пароль")
