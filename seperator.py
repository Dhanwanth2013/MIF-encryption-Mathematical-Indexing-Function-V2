import random as rd

digits2_choices = ['/', '<', '>', '?', ':']
digits3_choices = ['|', ';', '_', '-', '{']

def separator(string_list, seed=0):
    rng = rd.Random(seed)
    result = []
    for num in string_list:
        if len(num) == 2:
            sep = rng.choice(digits2_choices)
            result.append(sep.join(num))
        elif len(num) == 3:
            sep = rng.choice(digits3_choices)
            result.append(sep.join(num))
        else:
            result.append(num)
    return result
