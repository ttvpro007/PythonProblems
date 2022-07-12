import os
import re

def create_file(file_name):
    if not is_valid_file_name(file_name):
        print(f"'{file_name}' is NOT a valid file name. File name should include file extension e.g. 'your_file_name.exe'")
        return
        
    if os.path.exists(file_name):
        print(f"file '{file_name}' already exist at\n{os.path.abspath(file_name)}")
    else:
        open(file_name, 'w')
        print(f"file '{file_name}' created at\n{os.path.abspath(file_name)}")
    return



def delete_file(file_name):
    if not is_valid_file_name(file_name):
        print(f"'{file_name}' is NOT a valid file name. File name should include file extension e.g. 'your_file_name.exe'")
        return
        
    if not os.path.exists(file_name):
        print(f"file '{file_name}' does not exist at\n{os.getcwd()}")
    else:
        os.remove(file_name)
        print(f"file '{file_name}' removed from\n{os.getcwd()}")
    return


def is_valid_file_name(file_name):
    return re.search('\.[a-zA-Z]+$', file_name)
    
    
# create_file('codingbat_labs.py')
# create_file('test_create2.txt')
# delete_file('test_create2.txt')


"""
finding palindrome

palindrome(['racecar, hotdog, kayak, deed, run, fame, rotator, noon, tacocat']) → ['racecar, kayak, deed, rotator, noon, tacocat']
"""


def run_palindrome():
    with open('words_sorted.txt', 'r', encoding='utf-8') as f:
        words = [x.strip() for x in f]
    return [word for word in palindrome(words)]
    

def palindrome(words):
    for word in words:
        if len(word) > 2 and word == word[::-1]:
            yield word


"""
dynamic arguments
"""


def summation(*args):
    result = 0
    for arg in list(args):
        result += arg
        #print(arg)
    return result


#summation([n for n in range(10)])
#summation(1, 2, 3, 4, 5, 6, 7, 8, 9)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

def make_color(input_list):
    return ['\x1b[43m' + str(elem) if elem == 0 else '\x1b[0m' + str(elem) for elem in input_list]


# print('\033[0m, '.join(elem for elem in make_color(input_list)))


def remove_zeroes(input_list):
    zero_indices = []
    modified_zero_indices = []
    for index in range(len(input_list)):
        if input_list[index] == 0:
            zero_indices.append(index)
            modified_zero_indices.append(index - len(modified_zero_indices))
    
    print('\033[0m' + 'without modifying:', zero_indices)
    print('\033[0m' + 'with modifying:', modified_zero_indices)
    
    for index in modified_zero_indices:
        del input_list[index]


#from random import randrange
#remove_zeroes([(7 * randrange(0, 17) - i) % 3 for i in range(20)])


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

# print_format_table()


import colorama
def test_colorama(text):
    print(colorama.Back.WHITE + text + colorama.Back.BLACK)
    
# test_colorama('Hello World')


# binary sort for sorted list
# return index in list
# 1 - of the searched element
# or 
# 2 - that the searched element can be inserted into
def bi_search(arr, x, low = 0, high = None):
    if high == None:
        high = len(arr)
    if low < high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            return bi_search(arr, x, mid + 1, high)
        else:
            return bi_search(arr, x, low, mid)
    return low

# odd = True
# arr = [n for n in range(20) if n % 2 == odd]
# arr.insert(1, 2)
# print(arr)
# for a in arr:
#     print('searching for ', a + 1)
#     print('found at ', bi_search(arr, a + 1))
# print()
# print(arr)
# for a in arr:
#     print('searching for ', a)
#     print('found at ', bi_search(arr, a))
        

# Modify the list s in place so that all elements for which the
# given predicate pred is true are in the front in some order,
# followed by the elements for which pred is false, in some order.

def partition_in_place(s, pred):
    # Elements from position i to j, inclusive, can be anything.
    # Anything to left of i is acceptable, anything to the right
    # of j is unacceptable. When i == j, all is well.
    i, j = 0, len(s) - 1
    # Each round, one of the indices takes a step towards other.
    while i < j:
        # If s[i1] satisfies the predicate, leave it be...
        if pred(s[i]):
            i += 1
        else:
            # Otherwise, swap it to the end
            s[i], s[j] = s[j], s[i]
            j -= 1
    # Note that for list of n elements, pred is called exactly
    # n-1 times. This can be valuable if pred is expensive.
    return s

# s = ['Dick', 'Harry', 'Jerry', 'Einstein', 'Tom', 'Djickstra', 'Nintendo', 'Diana']

# print(partition_in_place(s, lambda x : len(x) > 5))


def prime_factorize(n):
    p = 2
    t = n
    primes = {}
    primes_product = 1
    while n > primes_product:
        # print(primes_product)
        if t % p == 0:
            t /= p
            if p not in primes:
                primes[p] = 1
            else:
                primes[p] += 1
            primes_product *= p
        else:
            p += 1
    return primes


# Babylonian method for finding square root
# integer only twist
def find_perfect_square(n):
    if n == 0: return 0
    if n == 1: return 1
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + n // x) // 2
        if x in seen: return None
        seen.add(x)
    return x


d = { "name":"John", "age":30, "city":"New York"}

create_file('cs109_module6_examples.py')
create_file('cs109_module6_examples_data.json')


