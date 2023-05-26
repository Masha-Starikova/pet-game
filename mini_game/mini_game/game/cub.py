import random


print("Добро пожалывать в игру Кубики. Правила игры:\n"
      "Ты выбераешь сколько кубиков мы брасаем от 1 до 5\n"
      "Затем ты можешь начать играть или выбрать другое количиство кубиков\n"
      "У кого сумарно выпадет больше тот и выйграл.")

# Функция выбора кубиков.
def choose_cub():
    num_cub = 0
    while num_cub < 1 or num_cub > 5:
        num_cub = int(input("Выберите количество кубиков (от 1 до 5): "))
        if num_cub < 1 or num_cub > 5:
            print("Некорректный ввод. Пожалуйста, выберите число от 1 до 5.")
    return num_cub

# Функция выброса кубиков.
def roll_cub(num_cub):
    results = []
    total_sum = 0
    for _ in range(num_cub):
        result = random.randint(1, 6)
        results.append(result)
        total_sum += result
    return results, total_sum


# Функция сравнивания результала и вывод.
def champion(num_cub):
    dice_results_1, total_1 = roll_cub(num_cub)
    dice_results_2, total_2 = roll_cub(num_cub)
    print(f"У меня выпало {num_cub} кубиков: {dice_results_1}\n"
          f"Сумма результата: {total_1}")
    print(f"У тебя выпало {num_cub} кубиков: {dice_results_2}\n"
          f"Сумма результата: {total_2}")
    if total_1 > total_2:
        print("Ты проиграл, повезет в следующий раз!")
        return 0
    elif total_1 == total_2:
        print("Поздравляю, у нас ничья!")
        return 0
    else:
        print('Поздравляю, ты выиграл!')
        return 1

def play():
    game = 0
    win = 0
    to_go = True
    while to_go:
        num_cub = choose_cub()
        if num_cub == 1:
            end = 'к'
        elif num_cub == 5:
            end = 'ков'
        else:
            end = 'ка'
        arg_play = input(f'Мы будем бросать {num_cub} куби{end}, играем? ').lower()
        while arg_play != 'да' and arg_play != 'нет':
            arg_play = input('Напиши "да" или "нет": ').lower()
        if arg_play == 'нет':
            change_cub = input('Хотите изменить количество кубиков? ').lower()
            while change_cub != 'да' and change_cub != 'нет':
                change_cub = input('Напиши "да" или "нет": ').lower()
            if change_cub == 'да':
                continue
            else:
                print('Спасибо за игру, до свидания!')
                break
        game += 1
        win += champion(num_cub)
        agr_restart = input('Сыграем еще? ').lower()
        while agr_restart != 'да' and agr_restart != 'нет':
            agr_restart = input('Напиши "да" или "нет": ').lower()
        if agr_restart == 'нет':
            print('Спасибо за игру, до свидания!')
            break
    return game, win

game, win = play()
print(f'Ты сыграл {game} раз, из них {win} раз победил.')
print('Спасибо за игру, до свидания!')
