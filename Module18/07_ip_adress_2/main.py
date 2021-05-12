def is_list_int(list_of_nums):
  for num in list_of_nums:
    if not num.isdigit():
      return True
  return False

def is_list_in_255(list_of_nums):
  for num in list_of_nums:
    if int(num) > 255 or int(num) < 0:
      return True
  return False

ip_string = input('Введите ip адрес: ')

is_ip_not_correct = True
while is_ip_not_correct:
  ip_list = ip_string.split('.')
  if len(ip_list) != 4:
    ip_string = input('Адрес - это четыре числа, разделённые точками: ')
  elif is_list_int(ip_list):
    ip_string = input('Присутствует не целое число: ')
  elif is_list_in_255(ip_list):
    ip_string = input('Число вне диапазона: ')
  else:
    print('IP-адрес корректен')
    is_ip_not_correct = False
