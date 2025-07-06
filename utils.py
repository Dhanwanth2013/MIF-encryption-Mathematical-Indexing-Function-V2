from string import ascii_lowercase, ascii_uppercase, punctuation, digits
import random as rd

mutation_prob = 0.5
char_set = ascii_lowercase + ascii_uppercase + punctuation + digits

def return_char_list(string_input):
    return [char for char in string_input]

def char_to_num(char_list):
    return [char_set.index(c) if c in char_set else 99 for c in char_list]

def MInt_function(num_list, key, mod):
    return [(x + key) % mod for x in num_list]

def Random_int_mutation(num_list, seed=0):
    rng = rd.Random(seed)
    mutated = []
    mutations = []
    for x in num_list:
        if x > 1:
            delta = rng.randint(1, min(50, x))
        else:
            delta = 1
        mutations.append(delta)
        mutated.append(str(x + delta))
    return mutated, mutations

def Random_char_mutation(num_list, key, seed=0):
    rng = rd.Random(seed)
    mutated_list = []
    for num in num_list:
        new_str = ''
        for char in str(num):
            if char.isdigit() and rng.random() < mutation_prob:
                offset = (int(char) + key) % len(char_set)
                new_str += char_set[offset]
            else:
                new_str += char
        mutated_list.append(new_str)
    return mutated_list
