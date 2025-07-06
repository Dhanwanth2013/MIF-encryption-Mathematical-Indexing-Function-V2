from utils import *
from seperator import separator

def encrypt_mif(text, key=17, seed=0, mod=997):
    char_list = return_char_list(text)
    nums = char_to_num(char_list)
    transformed = MInt_function(nums, key, mod)
    mutated, mutation_log = Random_int_mutation(transformed, seed)
    char_mutated = Random_char_mutation(mutated, key, seed + 1)
    final_encrypted = separator(char_mutated, seed + 2)
    return ''.join(final_encrypted), mutation_log

# Example usage
text = "This is a test message"
encrypted, mutations = encrypt_mif(text, key=17, seed=42)
print("Encrypted:", encrypted)
