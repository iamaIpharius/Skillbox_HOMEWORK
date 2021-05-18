violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_ad = int(input('Сколько песен? '))
total_time = 0
for i in range(1, songs_ad + 1):
    print('Введите название {num} песни: '.format(num=i), end='')
    song_name = input()
    if song_name in violator_songs:
        total_time += violator_songs[song_name]
    else:
        print('Такой песни не найдено')
print("Общее время звучания песен: {0} минут".format(round(total_time, 2)))
