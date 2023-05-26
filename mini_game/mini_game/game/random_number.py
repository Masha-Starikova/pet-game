from random import randint

MAX_N = 100
to_go = True
game = 0
totol_attempts = 0

print('Добро пожаловать в игру: Угадай число.')

while to_go:
    person_n = 0
    attempts = 0
    interval = input(f'Я загадал число от 1 до {MAX_N}. Хочешь поменять интервал? ')
    while interval != 'да' and interval != 'нет':
        interval = input('Напиши \"да\" или \"нет\": ')
    if interval == 'да':
        MAX_N = input("инервал будет от 1 до: ")
        while not MAX_N.isdigit() or not 1 <= int(MAX_N):
            MAX_N = input('Введите целое число больше 1: ')
    MAX_N = int(MAX_N)
    secret_n = randint(1, MAX_N)
    game += 1
    while person_n != secret_n:
        person_n = input("Какое число я загадал? ")
        while not person_n.isdigit() or not(1 <= int(person_n) <= MAX_N):
            person_n = input(f'Введите целое число от 1 до {MAX_N}: ')
        attempts += 1
        person_n = int(person_n)
        if person_n > secret_n:
            print('Мое число поменьше.')
        elif person_n < secret_n:
            print('Мое число побольше.')
    if 11 <= attempts % 100 <= 14:
        end = 'ок'
    elif attempts % 10 == 1:
        end = 'ку'
    elif attempts % 10 <= 4:
        end = 'ки'
    else:
        end = 'ок'
    totol_attempts += attempts
    print( f'Правильно! Это число: {secret_n}')
    print( f'Ты использовал {attempts} попыт{end}.')
    print( f'Ты сыграл {game} .')    
    again = input('Сыграем еще? ')
    while again != 'да' and again != 'нет':
        again = input('Напиши \"да\" или \"нет\": ')
    if again == 'нет':
        to_go = False

print('Спасибо за игру!')