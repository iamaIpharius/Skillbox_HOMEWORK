from collections import deque


def can_be_poly(string: str) -> bool:
    d_right = deque('')
    d_left = deque('')
    for elem in string.lower():
        if elem not in ' !@#$%^&*()_+"№;:?':
            d_right.append(elem)
            d_left.appendleft(elem)

    if d_left == d_right:
        return True
    return False


def can_be_poly2(string: str) -> bool:
    d_normal = deque(filter(lambda x: x not in ' !@#$%^&*()_+"№;:?', string.lower()))
    d_reverse = deque([x for x in reversed(d_normal)])

    if d_normal == d_reverse:
        return True
    return False


print(can_be_poly('saippuakivikauppias!'))
print(can_be_poly('а роза упала на лапу Азора'))
print(can_be_poly2('saippuakivikauppias!'))
print(can_be_poly2('а роза упала на лапу Азораff'))

