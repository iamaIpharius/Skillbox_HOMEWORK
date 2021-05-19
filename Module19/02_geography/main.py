countries_ad = int(input('Сколько стран? '))
result = dict()
for _ in range(countries_ad):
    current_country = input('Введите страну и города через пробел: ')
    current_list = current_country.split()
    current_dict = {current_list[i]: current_list[0] for i in range(1, len(current_list))}
    result.update(current_dict)


for _ in range(3):
    city = input('Введите город: ')
    if city in result:
        print('Город {city} расположен в стране {country}'.format(city=city, country=result[city]))
    else:
        print(f'По городу {city} данных нет.'.format(city=city))