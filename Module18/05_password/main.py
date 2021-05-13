def get_numbers_from_password(text):
  number_count = 0
  for letter in text:
    if letter.isdigit():
      number_count += 1
  if number_count >= 3:
    return False
  else:
    return True



password = input('Введите пароль: ')
password_is_bad = True
while password_is_bad:
  if len(password) < 8:
    password = input('Пароль ненадёжный. Попробуйте ещё раз. ')
  elif get_numbers_from_password(password):
    password = input('Пароль ненадёжный. Попробуйте ещё раз. ')
  elif password.islower():
    password = input('Пароль ненадёжный. Попробуйте ещё раз. ')
  else:
    password_is_bad = False
    print('Это надёжный пароль!')

