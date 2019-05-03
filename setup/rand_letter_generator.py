#Returns a list of randomly generated letters
import random

from lib.api_calls import *

def gen_rand_letters():
    #myfile = open("random_letters.txt", "w")

    legal_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    data = []

    i = 0
    while i < 1000:
        
        
        word_limit = random.randint(20, 30)
        j = 0
        word = ""
        while j < word_limit:
            index = random.randint(0, 25)
            word += legal_chars[index]
            j += 1

        data.append(word)
        i += 1

    write("random_letters", data)
    #print(output_list)
    #return output_list

gen_rand_letters()