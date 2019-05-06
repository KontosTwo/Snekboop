#Returns a list of randomly generated letters
import random

from lib.api_calls import *
from functions.test.sequential_function1 import *
from functions.test.sequential_function2 import *
from functions.test.sequential_function3 import *

import time
def benchmark():

    data1 = generate_and_return(20)
    data2 = generate_and_return(200)
    data3 = generate_and_return(2000)




    start_time = time.time()
    query("test1","reverse")
    print("--- 20 strings using reverse %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    reverse(data1)
    print("--- sequential 20 strings using reverse %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    query("test2", "reverse")
    print("--- 200 strings using reverse %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    reverse(data2)
    print("--- sequential 200 strings using reverse %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    query("test3", "reverse")
    print("--- 2000 strings using reverse %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    reverse(data3)
    print("--- sequential 2000 strings using reverse %s seconds ---" % (time.time() - start_time))


    start_time = time.time()
    query("test1","sort_find")
    print("--- 20 strings using sort_find %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    sort_find(data1)
    print("--- sequential 20 strings using reverse %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    query("test2", "sort_find")
    print("--- 200 strings using sort_find %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    sort_find(data2)
    print("--- sequential 200 strings using reverse %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    query("test3", "sort_find")
    print("--- 2000 strings using sort_find %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    sort_find(data3)
    print("--- sequential 2000 strings using reverse %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    query("test1", "lcs")
    print("--- 20 strings using lcs %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    lcs(data1)
    print("--- sequential 20 strings using lcs %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    query("test2", "lcs")
    print("--- 200 strings using lcs %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    lcs(data2)
    print("--- sequential 200 strings using lcs %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    query("test3", "lcs")
    print("--- 2000 strings using lcs %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    lcs(data3)
    print("--- sequential 2000 strings using lcs %s seconds ---" % (time.time() - start_time))


def generate(name, number):
    legal_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]

    data = []

    i = 0
    while i < number:
        word_limit = random.randint(20, 30)
        j = 0
        word = ""
        while j < word_limit:
            index = random.randint(0, 25)
            word += legal_chars[index]
            j += 1

        data.append(word)
        i += 1
    write(name, data)

def generate_and_return(number):
    legal_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]

    data = []

    i = 0
    while i < number:
        word_limit = random.randint(20, 30)
        j = 0
        word = ""
        while j < word_limit:
            index = random.randint(0, 25)
            word += legal_chars[index]
            j += 1

        data.append(word)
        i += 1
    return data

def generate_all():
    generate("test1", 20)
    generate("test2", 200)
    generate("test3", 2000)


benchmark()