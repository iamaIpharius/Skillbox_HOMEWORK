def get_fibo_by_pos(pos, start=0, step=1):
    if pos == 0:
        return start
    start, step = step, start + step
    pos -= 1
    return get_fibo_by_pos(pos, start, step)


num_pos = int(input('Введите позицию: '))

print(get_fibo_by_pos(num_pos))