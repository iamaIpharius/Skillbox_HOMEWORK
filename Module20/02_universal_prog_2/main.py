def is_prime(count):
    if count == 0:
        return False
    for i in range(2, count):
        if count % i == 0:
            return False
    return True


def prime_items_list(list_of_something):
    return [item for id_of_item, item in enumerate(list_of_something) if is_prime(id_of_item)]


