site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def find_key(dictionary, key, depth=None):
    if key in dictionary:
        return dictionary[key]
    if isinstance(depth, int):
        depth -= 1
        if depth == 0:
            return None
    for sub_d in dictionary.values():
        if isinstance(sub_d, dict):
            result = find_key(sub_d, key, depth)
            if result:
                break
    else:
        result = None
    return result

my_key = input('Введите ключ: ')
my_depth = int(input('Введите глубину (если 0, то глубина не задана): '))
if my_depth == 0:
    my_depth = None
answer = find_key(site, my_key, my_depth)
if answer:
    print(answer)
else:
    print('Нет такого')