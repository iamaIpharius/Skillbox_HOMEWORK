import re

numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

privat_pattern = r'\b\w{1}\d{3}\w{2}\d{2,3}\b'
taxi_pattern = r'\b\w{2}\d{3}\d{2,3}\b'

p_result = re.findall(privat_pattern, numbers)
t_result = re.findall(taxi_pattern, numbers)

print('Частиные номера', p_result)
print('Номера такси', t_result)