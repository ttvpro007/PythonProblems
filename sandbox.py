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


def remove(input_list, element_to_remove):
    
    zero_indices = []
    modified_zero_indices = []
    
    for index in range(len(input_list)):
        
        if input_list[index] == element_to_remove:
            zero_indices.append(index)
            modified_zero_indices.append(index - len(modified_zero_indices))
    
    print('\033[0m' + 'without modifying:', zero_indices)
    print('\033[0m' + 'with modifying:', modified_zero_indices)
    
    for index in modified_zero_indices:
        del input_list[index]


#from random import randrange
#remove([(7 * randrange(0, 17) - i) % 3 for i in range(20)])


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


# d = { "name":"John", "age":30, "city":"New York"}

# create_file('cs109_module6_examples.py')
# create_file('cs109_module6_examples_data.json')


def count(x, terminating_condition, step):
    
    y = x + step
    
    if step == 0:
        return terminating_condition
    
    elif step < 0:
        print(y)
        if y > terminating_condition:
            return count(y, terminating_condition, step)
        else:
            return y
    
    elif step > 0:
        print(y)
        if y < terminating_condition:
            return count(y, terminating_condition, step)
        else:
            return y
        
    


# print(count(10, 1, 1))


# from hashlib import sha256

# chk = sha256()
# chk.update(str(750).encode('utf-8'))
# digest = chk.hexdigest()
# print(digest[:])

# import sys

# print(sys.executable)

# class Crab:
#     def __init__(self, value, left = None, right = None):
#         self.value = value
#         self.left = left
#         self.right = right
#     def __key(self):
#         return (self.value)
#     def __hash__(self):
#         return hash(self.__key())
#     def __lt__(self, other):
#         return self.value < other.value
#     def __le__(self, other):
#         return self.value <= other.value
#     def __gt__(self, other):
#         return self.value > other.value
#     def __ge__(self, other):
#         return self.value >= other.value
#     def __eq__(self, other):
#         if not other:
#             return self.value == None
#         return self.value == other.value

# # A special doubly linked list
# class CrabList:
#     def __init__(self, head = None):
#         self._head = head
#         self._tail = self._head
#     def __iter__(self):
#         return self.move_right()
#     def _link_crabs(self, left_crab, right_crab):
#         if left_crab: left_crab.right = right_crab
#         if right_crab: right_crab.left = left_crab
#     def add(self, data):
#         crab = Crab(data)
#         if self._head == None:
#             self.__init__(crab)
#         else:
#             self._link_crabs(self._tail, crab)
#             self._tail = self._tail.right
#         return crab
#     def move_right(self):
#         current_crab = self._head
#         while current_crab:
#             yield current_crab
#             current_crab = current_crab.right
#     def crabs_to_remove(self, base_crab):
#         if base_crab.left and base_crab.right:
#             return base_crab, base_crab.left if base_crab.left > base_crab.right else base_crab.right
#         else:
#             return base_crab, base_crab.left if base_crab.left else base_crab.right
#     def remove_crab(self, crab_to_remove):
#         if not crab_to_remove: pass
#         if crab_to_remove == self._head:
#             self._head = self._head.right
#         if crab_to_remove == self._tail:
#             self._tail = self._tail.left
#         left_crab = crab_to_remove.left
#         right_crab = crab_to_remove.right
#         if left_crab: left_crab.right = right_crab
#         if right_crab: right_crab.left = left_crab
#         crab_to_remove.left = None
#         crab_to_remove.right = None
#         return crab_to_remove

# def eliminate_neighbours(items):
#     crab_list = CrabList()
#     item_value_to_crab_dict = {} # item value: crab
#     # removed_crabs = set()
#     removed_values = set()
#     for i in range(len(items)):
#         item_value_to_crab_dict[ items[i] ] = crab_list.add( items[i] )
#     largest_crab = max(crab_list)
#     current_smallest_item_value = 1
#     count = 1
#     while True:
#         smallest_crab = item_value_to_crab_dict[ current_smallest_item_value ]
#         if smallest_crab == largest_crab: break
#         crab1, crab2 = crab_list.crabs_to_remove(smallest_crab)
#         if crab1 == largest_crab or crab2 == largest_crab: break
#         removed_values.add( crab_list.remove_crab( crab1 ).value )
#         removed_values.add( crab_list.remove_crab( crab2 ).value )
#         # while item_value_to_crab_dict[ current_smallest_item_value ] in removed_crabs:
#         while current_smallest_item_value in removed_values:
#             current_smallest_item_value += 1
#         count += 1
#     return count


class Crab:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        left_str, right_str = self.get_neighbours_str()
        return f'Crab({left_str}, {str(self.value)}, {right_str})'
    def __key(self):
        return self.value
    def __hash__(self):
        return hash(self.__key())
    def __lt__(self, other):
        return self.value < other.value
    def __le__(self, other):
        return self.value <= other.value
    def __gt__(self, other):
        return self.value > other.value
    def __ge__(self, other):
        return self.value >= other.value
    def __eq__(self, other):
        if not other:
            return self.value == None
        return self.value == other.value


# A special doubly linked list
class CrabList:
    def __init__(self, head = None):
        self._head = head
        self._tail = self._head
    def __iter__(self):
        return self.move_right()
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return str([item for item in self.__iter__()])
    def _link_crabs(self, left_crab, right_crab):
        if left_crab: left_crab.right = right_crab
        if right_crab: right_crab.left = left_crab
    def add(self, data):
        crab = Crab(data)
        if self._head == None:
            self.__init__(crab)
        else:
            self._link_crabs(self._tail, crab)
            self._tail = self._tail.right
        return crab
    def move_right(self):
        current_crab = self._head
        while current_crab:
            yield current_crab
            current_crab = current_crab.right
    def crabs_to_remove(self, base_crab):
        if base_crab.left and base_crab.right:
            return base_crab, base_crab.left if base_crab.left > base_crab.right else base_crab.right
        else:
            return base_crab, base_crab.left if base_crab.left else base_crab.right
    def remove_crab(self, crab_to_remove):
        if not crab_to_remove: pass
        if crab_to_remove == self._head:
            self._head = self._head.right
        if crab_to_remove == self._tail:
            self._tail = self._tail.left
        left_crab = crab_to_remove.left
        right_crab = crab_to_remove.right
        if left_crab: left_crab.right = right_crab
        if right_crab: right_crab.left = left_crab
        crab_to_remove.left = None
        crab_to_remove.right = None
        return crab_to_remove


def eliminate_neighbours(items):
    crab_list = CrabList()
    item_value_to_crab_dict = {} # item value: crab
    # removed_crabs = set()
    removed_values = set()
    for i in range(len(items)):
        item_value_to_crab_dict[ items[i] ] = crab_list.add( items[i] )
    largest_crab = max(crab_list)
    current_smallest_item_value = 1
    count = 1
    while True:
        smallest_crab = item_value_to_crab_dict[ current_smallest_item_value ]
        if smallest_crab == largest_crab: break
        crab1, crab2 = crab_list.crabs_to_remove(smallest_crab)
        if crab1 == largest_crab or crab2 == largest_crab: break
        removed_values.add( crab_list.remove_crab( crab1 ).value )
        removed_values.add( crab_list.remove_crab( crab2 ).value )
        # while item_value_to_crab_dict[ current_smallest_item_value ] in removed_crabs:
        while current_smallest_item_value in removed_values:
            current_smallest_item_value += 1
        count += 1
    return count


# line 2587 in tester109
# def eliminate_neighbours(items):
    
#     # handles length 1
#     if len(items) < 2:
#         return 1
    
#     index_nodes = [] # this acts as doubly linked list
#     element_dict = {} # keeps track of element indices and seen status
    
#     current_smallest_item = 1
#     largest_item = max(items)
#     largest_seen = 1
#     count = 0
    
#     # populate index nodes
#     for i in range(len(items)):
#         left_index = i - 1 if i - 1 >= 0 else None
#         left_node = index_nodes[ left_index ] if left_index != None else None
#         curr_node = Node( items[i] )
#         curr_node.left_node = left_node
        
#         if left_node != None:
#             left_node.right_node = curr_node
            
#         index_nodes.append( curr_node )
        
#         element_dict[ items[ i ] ] = {'index': i, 'seen': False}
        
#     while largest_seen != largest_item:
        
#         # remove biggest neighbor node
#         current_smallest_item_node = index_nodes[ element_dict[ current_smallest_item ][ 'index' ] ]
        
#         left_node = current_smallest_item_node. left_node
        
#         right_node = current_smallest_item_node. right_node
        
#         biggest_neighbor_node = None
        
#         if not left_node:
#             biggest_neighbor_node = right_node
            
#         elif not right_node:
#             biggest_neighbor_node = left_node
            
#         else:
#             biggest_neighbor_node = left_node if left_node. data > right_node. data else right_node
        
#         if biggest_neighbor_node:
#             largest_seen = biggest_neighbor_node. data
#             element_dict[ largest_seen ][ 'seen' ] = True
#             remove_node( biggest_neighbor_node )
        
#         # remove current smallest item
#         element_dict[ current_smallest_item ][ 'seen' ] = True
#         remove_node( current_smallest_item_node )
        
#         count += 1
        
#         if current_smallest_item == largest_item:
#             break
        
#         while current_smallest_item < largest_item and element_dict[ current_smallest_item ][ 'seen' ] == True:
#             current_smallest_item += 1
        
#     return count


# def remove_node(curr_node):
#     if curr_node:
    
#         left_node = curr_node.left_node
        
#         right_node = curr_node.right_node
        
#         # if there is a left node
#         # set the right node of that left node
#         # to be the right node of current node
#         if left_node:
#             left_node.right_node = right_node
        
#         # if there is a right node
#         # set the left node of that right node
#         # to be the left node of current node
#         if right_node:
#             right_node.left_node = left_node
        
#         # now we remove the connection of the
#         # current node to its left and right nodes
#         curr_node.left_node = None
#         curr_node.right_node = None


# # line 2588 in tester109
# def eliminate_neighbours(items):
    
#     # handles length 1
#     if len(items) < 2:
#         return 1
    
#     item_value_nodes = DoublyLinkedList()
#     element_dict = {}
#     current_smallest_item = 1
#     largest_item = max(items)
#     largest_seen = 1
#     count = 0
    
#     # populate index nodes and position dictionary
#     for i in range(len(items)):
#         item_value_nodes.add(Node(items[i]))
#         element_dict[ items[ i ] ] = {'index': i, 'seen': False}
        
#     while largest_seen < largest_item:
        
#         # remove biggest neighbor node
#         current_smallest_item_node = item_value_nodes[ element_dict[ current_smallest_item ][ 'index' ] ]
        
#         left_node = current_smallest_item_node. left_node
#         right_node = current_smallest_item_node. right_node
        
#         biggest_neighbor_node = None
        
#         if not left_node:
#             biggest_neighbor_node = right_node
            
#         elif not right_node:
#             biggest_neighbor_node = left_node
            
#         elif left_node and right_node:
#             biggest_neighbor_node = left_node if left_node. data > right_node. data else right_node
        
#         if biggest_neighbor_node:
#             largest_seen = biggest_neighbor_node. data
#             # record the largest_seen as seen = True
#             element_dict[ largest_seen ][ 'seen' ] = True
#             item_value_nodes.remove( biggest_neighbor_node )
        
#         # record the current_smallest_item as seen = True
#         element_dict[ current_smallest_item ][ 'seen' ] = True
#         # remove current smallest item
#         item_value_nodes.remove( current_smallest_item_node )
        
#         count += 1
        
#         if current_smallest_item == largest_item:
#             break
        
#         # increment the smallest item until its value has not been seen in the record
#         while current_smallest_item < largest_item and element_dict[ current_smallest_item ][ 'seen' ] == True:
#             current_smallest_item += 1
        
#     return count

    
# print(eliminate_neighbours( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ))
# print(eliminate_neighbours( range(1, 10001) ))
# print(eliminate_neighbours( [2, 1, 3] ))
# print(eliminate_neighbours( [1, 2, 3, 4] ))


def manhattan_skyline(towers):
    # print(towers)
    # points = []
    # for tower in towers:
    #     points += [ { 'x': tower[0], 'y': tower[2], 'pos': 'start' } ]
    #     points += [ { 'x': tower[1], 'y': tower[2], 'pos': 'end' } ]
    # points = sorted( points, key = lambda x : x['x'] )
    
    # current_x, current_y, total_area = 0, 0, 0
    # active_ys = [0]

    # for point in points:
    #     # if is start point
    #     if point['pos'] == 'start':
    #         active_ys.append( point['y'] )
            
    #         # if point.x is larger than current x
    #         if point['x'] >= current_x:
    #             current_x = point['x']
                
    #             # if point.y is larger than current y
    #             if point['y'] > current_y:
    #                 current_y = point['y']
    #     # if is end point
    #     elif point['pos'] == 'end':
    #         active_ys.remove( point['y'] )
    #         current_max_active_y = max(active_ys)
            
    #         if current_max_active_y < current_y:
    #             current_y = current_max_active_y
        
    return total_area 
