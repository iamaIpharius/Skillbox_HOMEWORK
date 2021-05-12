password = input('Введите пароль: ')
password_is_bad = True
while password_is_bad:
  if len(password) < 8:
    password = input('Пароль ненадёжный. Попробуйте ещё раз. ')
  elif password.isalpha():
    password = input('Пароль ненадёжный. Попробуйте ещё раз. ')
  elif password.islower():
    password = input('Пароль ненадёжный. Попробуйте ещё раз. ')
  else:
    password_is_bad = False
    print('Это надёжный пароль!')

