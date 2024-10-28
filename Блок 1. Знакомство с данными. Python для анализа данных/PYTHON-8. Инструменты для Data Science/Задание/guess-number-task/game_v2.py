"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
from typing import Callable

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def random_predict_with_correction(number: int = 1) -> int:
    """Рандомно угадываем число  с коррекцией меньше-больше

    Коррекция меньше-больше подразумевает, что мы корректируем верхнюю (если загаданное число меньше)
    или нижнюю (если загаданное число больше) границу, так как загадывать число за пределами границ
    бессысленно

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    # Начальное число для генератора
    first_number = 1
    # Конечное число для генератора
    last_number = 101  

    while True:
        count += 1
        predict_number = np.random.randint(first_number, last_number)
        if number == predict_number:
            # Если угадали - выходим из цикла
            break
        elif number < predict_number:
            # Коррекция верхней границы
            last_number = predict_number
        elif number > predict_number:
            # Коррекция нижней границы
            first_number = predict_number + 1
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score



def score_game_v2(*random_predict_algorythms: Callable, tryes_count: int=1000) -> list:
    """Сравнение количества попыток угадывания списка алгоритмов

    Args:
        random_predict_algirithms: список функций угадывания
        tryes_count (int, optional, default: 1000): количество итераций угадывания 

    Returns:
        list: (string, int) наименование алгоритма, среднее количество попыток
    """
    result = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(tryes_count))  # загадали список чисел


    for algorythm in random_predict_algorythms:
        name = algorythm.__name__
        for number in random_array:
            counts_list = algorythm(number)
            
        score = int(np.mean(counts_list))
        result.append((name, score))

    # print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return result

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
