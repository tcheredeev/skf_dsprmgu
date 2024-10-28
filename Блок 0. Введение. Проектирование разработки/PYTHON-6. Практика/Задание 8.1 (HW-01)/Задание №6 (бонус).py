# ваш код здесь
import string

s = input('Введите строку: ')

#
# Настройки программы
#

# Установка всех значения настроек в значение по умолчанию приводят вывод программы
# в соответствие с параметрами в описании задания

#
case_insensitive_search = True

#
alphabet = string.ascii_lowercase

#
# Объявления функций
#
def process(s):
  global alphabet
  idx = -1
  while True:
    idx += 1
    if idx >= len(s):
      break
    verify_char = s[idx]
    for i, char in enumerate(s[idx+1:]):
      if char == verify_char:
        s = s[:i+idx+1] + s[i+idx+2:]
        s = s[:idx] + s[idx+1:]
        alph_pos = alphabet.index(char) + 1 if alphabet.index(char) + 1 < len(alphabet) else 0
        s += alphabet[alph_pos]
        idx = -1
        break
  return s


def replace_duplicates(s):
  if case_insensitive_search:
    s = s.lower()
  s = process(s)
  return s

#
# Программа
#

print(replace_duplicates(s))
