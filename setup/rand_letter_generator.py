#Returns a list of randomly generated letters
import random

import lib.api_calls


#myfile = open("random_letters.txt", "w")

legal_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

data = []

i = 0
while i < 1000000:
    index = random.randint(0, 25)
    #myfile.write("test")
    data.append(legal_chars[index])
    i += 1

write_call("random_letters", data)
#print(output_list)
#return output_list

