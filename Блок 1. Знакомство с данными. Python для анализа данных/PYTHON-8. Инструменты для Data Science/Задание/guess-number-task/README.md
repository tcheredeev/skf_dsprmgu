# Проект "Угадай число"

## Оглавление  
[1. Описание проекта](README.md#Описание-проекта)  
[2. Какой кейс решаем?](README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](README.md#Этапы-работы-над-проектом)  
[5. Результат](README.md#Результаты)    
[6. Выводы](README.md#Выводы) 


### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток


**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.


**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений


**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
На начало проекта были даны 2 функции:
- **random_predict** - функция угадывания номера
- **score_game** - функция подсчёта среднего значения количества попыток угадывания
  
[к оглавлению](README.md#Оглавление)


### Этапы работы над проектом  
1) Написана функция **random_predict_with_correction** работающая по алгоритму коррекции больше-меньше
2) Написана функция **score_game_v2** принимающая в качестве значений ***функции - алгоритмы угадывания числа*** и возвращающая значения среднего количества попыток угадывания для них. Так же функция принимает именованный параметр ***tryes_count*** позволяющий задавать размерность массива загадываемых чисел 
3) Для репрезентативности была добавлена методом копипаста функция **game_core_v2** из гугл коллаб блокнота [baseline](https://colab.research.google.com/drive/1k2WZD8PWWOYFHrpAJoB2eZw06ID7KnFA) к видеоуроку

[к оглавлению](README.md#Оглавление)


### Результаты
Всё работает.

Задача по уменьшению среднего количества угадываний до <20 выполнена.

Цели урока достигнуты.

[к оглавлению](README.md#Оглавление)


### Выводы:  
-

[к оглавлению](README.md#Оглавление)
