# Вычислитель сложности пароля

Принимает на вход путь к файлу с паролем и путь к словарю с часто используемымы паролями и выводит оценку от 1 до 10, где 1 – очень слабый пароль и 10 – сильный.

# Критерии оценивания

1. Использование и заглавных и строчных букв – 2 балла
2. Использование спецсимволов ``` !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ``` – 2 балла
3. Длина пароля
  * До 12 символов – 0 баллов
  * От 12 до 14 символов – 1 балл
  * Более 14 символов – 2 балла
4. [Черный список](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10k_most_common.txt) паролей
  * Пароль входит в черный список – 0 баллов (окончательная оценка)
  * Пароль из черного списка является подстрокой проверяемого пароля (или наоборот) – 1 балл
  * Ни то, и ни другое условие не выполнено – 2 балла
5. Не использование дат в пароле – 2 балла

# Запуск и пример работы

Запуск на Linux:

```#!bash
$ python3 password_strength.py <path_to_file_with_password> <path_to_file_with_dict>
```
Запуск на Windows происходит аналогично.

Примеры работы:

```#!bash
$ python3 password_strength.py password.txt common_passwords.txt
Ваша оценка – 10 из 10
```
Пример [файла с паролем](https://pastebin.com/raw/aryPNpzf)

Справка:
```#!bash
python3 password_strength.py -h
usage: password_strength.py [-h] passfilepath dictfilepath

positional arguments:
  passfilepath  Path to file with password
  dictfilepath  Path to file with common password

optional arguments:
  -h, --help    show this help message and exit
```

Рекомендуется использовать [этот словарь](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10k_most_common.txt).

# Цели проекта

Это код написан в образовательных целях. Тренировачный курс для веб-девелоперов - [DEVMAN.org](https://devman.org)
