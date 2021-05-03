violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_ad = int(input('Сколько песен? '))
total_time = 0
for song_num in range(songs_ad):
    print('Введите название', song_num + 1, 'песни:', end=' ')
    song = input()
    for violator_song in violator_songs:
        if song == violator_song[0]:
            total_time += violator_song[1]

print('Общее время звучания песен:', round(total_time, 2), 'минут')