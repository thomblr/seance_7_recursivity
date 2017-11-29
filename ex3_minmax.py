def get_min_max(list_integers, minimum=-1, maximum=-1, nb_min=0, nb_max=0):
    if len(list_integers) == 0:
        return minimum, maximum, nb_min, nb_max
    else:
        to_check = list_integers[0]

        if to_check > maximum or maximum == -1:
            maximum = to_check
        elif to_check == maximum:
            nb_max += 1

        if to_check < minimum or minimum == -1:
            minimum = to_check
        elif to_check == minimum:
            nb_min += 1

        return get_min_max(list_integers[1:], minimum, maximum, nb_min, nb_max)


print(get_min_max([2, 2, 5, 1, 13, 34, 54, 34, 7, 1, 1]))
