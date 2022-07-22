import numpy, fractions, collections, bisect


# helper classes
class Node:
    def __init__(self, data):
        self._data = data
        self._left_node = None
        self._right_node = None
        
    def __repr__(self):
        return self._data
        
    @property       # getter
    def data(self):
        return self._data
    @data.setter    # setter
    def data(self, data):
        self._data = data
    
    @property
    def left_node(self):
        return self._left_node
    @left_node.setter
    def left_node(self, left_node):
        self._left_node = left_node
        
    @property
    def right_node(self):
        return self._right_node
    @right_node.setter    
    def right_node(self, right_node):
        self._right_node = right_node
        
        
class DoublyLinkedList:
    def __init__(self, head : Node = None):
        self._head : Node = head
        self._tail : Node = head
        self._items = []
        
        if head:
            self._link_nodes(self._head, self._tail)
            self._items += [self._head]
    
    # implement this to make class iterable
    def __iter__(self):
        return self.traverse_right()
    
    # implement this to use subscript and get value
    # for example my_var = my_list[0]
    def __getitem__(self, index):
        return self._items[index]
    
    # implement this to use subscript and set value
    # for example my_list[0] = my_val
    def __setitem__(self, index, node):
        if node == None:
            raise ValueError('Node cannot be None')
        
        node_at_index = self.__getitem__(index)
        left_node = node_at_index.left_node
        right_node = node_at_index.right_node
        
        # remove first because remove adjust the links
        # for the left and right node of the removed node
        # therefore if link the new node first, the
        # adjustment in remove will nullify the changes
        self.remove(node_at_index)
        
        self._link_nodes(left_node, node)
        self._link_nodes(node, right_node)
        
        
        self._items[index] = node
    
    # implement this to utilize the len() function for length
    def __len__(self):
        return len(self._items)
    
    # this link nodes together
    def _link_nodes(self, left_node : Node, right_node : Node):
        left_node.right_node = right_node
        right_node.left_node = left_node
    
    def add(self, node):
        if self._head == None:
            self.__init__(node)
        else:
            self._link_nodes(self._tail, node)
            self._tail = self._tail.right_node
            self._items.append(self._tail)
    
    # a generator for traversing the list from left to right
    def traverse_right(self):
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node.right_node
    
    # a generator for traversing the list from right to left
    def traverse_left(self):
        current_node = self._tail
        while current_node:
            yield current_node
            current_node = current_node.left_node
    
    # remove a node from list
    def remove(self, node_to_remove):
        if node_to_remove:
        
            left_node = node_to_remove.left_node
            
            right_node = node_to_remove.right_node
            
            # if there is a left node
            # set the right node of that left node
            # to be the right node of current node
            if left_node:
                left_node.right_node = right_node
            
            # if there is a right node
            # set the left node of that right node
            # to be the left node of current node
            if right_node:
                right_node.left_node = left_node
            
            # delete the current node
            del node_to_remove


# helper functions
def get_list_without_element_at_index(l, i):
    if i not in range(len(l)):
        raise IndexError
    if i == 0:
        return l[ 1 : len(l) ]
    elif i == len(l) - 1:
        return l[ : -1]
    return l[ 0 : i ] + l[ i + 1 : len(l) ]


def get_element_index_dict(items):
    d = {}
    for i in range(len(items)):
        if items[i] not in d:
            d[items[i]] = [i]
        else:
            d[items[i]].append(i)
    return d


def get_element_frequency_dict(items):
    d = {}
    for item in items:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d


def remove_element_with_value(input_list, element_to_remove):
    
    element_to_remove_indices_indices = []
    
    for index in range(len(input_list)):
        
        if input_list[index] == element_to_remove:
            element_to_remove_indices_indices.append(index - len(element_to_remove_indices_indices))
    
    for index in element_to_remove_indices_indices:
        del input_list[index]
        
    return input_list


def get_inverted_permutation(perm):
    
    inv_perm = [0] * len(perm)
    
    for i in range(len(perm)):
        inv_perm[perm[i]] = i
        
    return inv_perm


def get_duplicate_numbers(number):
    
    number_string = str(number)
    start = -1
    number_blocks = []
    
    for i in range(len(number_string) - 1):
        
        # if number repeated
        if number_string[i] == number_string[i + 1]:
            # set flag start at index i
            if start == -1:
                start = i
        
        # if number not repeated and flag start has already been set
        elif start != -1:
            # append the block of number from index start to index i + 1
            number_blocks.append(''.join(number_string[start : i + 1]))
            start = -1
        
        # use this block of code to check within the loop and not the for...else block
        # if start != -1 and i == len(number_string) - 2:
        #     number_blocks.append(''.join(number_string[start : i + 2]))
        
    else:
        # this check for duplicate numbers that appear at the end
        # if is at the end of string, and flag start has already been set
        # we take the block of number from index start to index i + 2
        if start != -1:
            number_blocks.append(''.join(number_string[start : i + 2]))
            
    return number_blocks


def get_distinct_numbers(number):
    
    number_string = str(number)
    start = -1
    number_blocks = []
    
    for i in range(len(number_string) - 1):
        
        # if number repeated
        if number_string[i] == number_string[i + 1]:
            # set flag start at index i
            if start == -1:
                start = i
        
        # if number not repeated and flag start has already been set
        elif start != -1:
            # append the block of number from index start to index i + 1
            number_blocks.append(''.join(number_string[start : i + 1]))
            start = -1
        
        # if number not repeated and flag has not been set
        elif start == -1:
            # append that number
            number_blocks.append(number_string[i])
        
        # use this block of code to check within the loop and not the for...else block
        # if start != -1 and i == len(number_string) - 2:
        #     number_blocks.append(''.join(number_string[start : i + 2]))
        
    else:
        # this check for duplicate numbers that appear at the end
        # if is at the end of string, and flag start has already been set
        # we take the block of number from index start to index i + 2
        if start != -1:
            number_blocks.append(''.join(number_string[start : i + 2]))
        else:
            number_blocks.append(number_string[i + 1])
            
    return number_blocks


"""
Ryerson Letter Grade - page 10
"""


def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


"""
Ascending list - page 11
"""


def is_ascending(items):
    if len(items) < 2:
        return True
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False
    return True


"""
Riffle shuffle kerfuffle - page 12
"""


def riffle(items, out = True):
    n = len(items) // 2
    result = []
    list1, list2 = items[:n], items[n:]
    for i in range(n):
        result.append(list1[i] if out else list2[i])
        result.append(list2[i] if out else list1[i])
    return result


"""
Even the odds - page 13
"""


def only_odd_digits(n):
    return all([int(n) % 2 == 1 for n in str(n)])


"""
Cyclops numbers - page 14
"""


def is_cyclops(n):
    if n == 0:
        return True
    without_zero = str(n).split('0')
    return 1 < len(without_zero) < 3 and len(without_zero[0]) == len(without_zero[1])


"""
Domino cycle - page 15
"""


def domino_cycle(tiles):
    if len(tiles) == 1:
        return tiles[0][0] == tiles[0][1]
    for i in range(len(tiles)):
        if tiles[i][1] != tiles[(i + 1) % len(tiles)][0]:
            return False
    return True


"""
Colour trio - page 16
"""


def colour_trio(colours):
    if len(colours) <= 1:
        return colours
    new_colour = ''
    for i in range(len(colours) - 1):
        new_colour += get_mixed_colour(colours[i], colours[i + 1])
    return colour_trio(new_colour)

def get_mixed_colour(colour1, colour2):
    if colour1 == colour2:
        return colour1
    for colour in ['r', 'b', 'y']:
        if colour1 != colour and colour2 != colour:
            return colour


"""
Count dominators - page 17
"""


def count_dominators(items):
    if len(items) == 0:
        return 0
    
    count = 1
    current_max = items[len(items) - 1]
    
    for i in range(len(items) - 2, -1, -1):
        if items[i] > current_max:
            count += 1
            current_max = items[i]
            
    return count


"""
Beat the previous - page 18
"""


def extract_increasing(digits):
    
    result = [int(digits[0])]    
    i = 1
    
    while i < len(digits):
    # for i in range(len(digits)):
        
        num = digits[i]
        
        while int(num) <= result[len(result) - 1] and i < len(digits) - 1:
            i += 1
            num += digits[i]
            
        if int(num) > result[-1:][0]:
            result.append(int(num))
            
        i += 1
        
    return result


"""
Subsequent words - page 19
"""


def words_with_letters(words, letters):
    
    result = []
    for word in words:
        if check_word_with_letters(word, letters):
            result.append(word)
            
    return result


def check_word_with_letters(word, letters):
    
    # remove invalid cases
    if len(word) < len(letters):
        return False
    
    # return true only when is exact match
    if len(word) == len(letters):
        return word == letters
    
    # narrow search window in the word for first letter of letters sequence
    # then store last match index if we got a matching letter in the word to start next search from there
    # e.g. 'brohiic' and 'bronchiectatic' we search 'b' in the first 8 letters of 'bronchiectatic' only
    # since if we don't have any match for letter 'b' after 8 letters, that word is invalid
    #        0123456
    #        brohiic
    # bronchiectatic
    # 01234567
    # the letter 'b' at index 0 of letters will be compared to the first 8 letters (index 0-7) in the sample word
    
    match_count = 0
    last_match_index = -1
    
    for i in range(len(letters), 0, -1):
        
        # as we iterate throuth the letters, we expand the search window for the next letter
        start_search_index = last_match_index + 1 if -1 < last_match_index else 0
        
        for j in range(start_search_index, len(word) - i + 1):
            if letters[len(letters) - i] == word[j]:
                match_count += 1
                last_match_index = j
                break
            
            # if reached the end of search but match count does not match 
            # the number of letter searched we return false
            if j == len(word) - i != match_count:
                return False
            
    return match_count == len(letters)


"""
Taxi ℤum ℤum - page 20
"""


def taxi_zum_zum(moves):
    
    # 4 directions represented as (x, y)
    four_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    current_position = (0, 0)
    
    for move in moves:
        
        if move == 'R':
            current_direction += 1
            
        if move == 'L':
            current_direction -= 1
            
        if move == 'F':
            current_position = get_new_position(current_position, four_directions[current_direction % 4])
            
    return current_position


def get_new_position(current_position, direction):
    return (current_position[0] + direction[0], current_position[1] + direction[1])


"""
Exact change only - page 21
"""


def give_change(amount, coins):
    
    change = []
    for coin in coins:
        
        coin_needed = amount // coin
        
        for i in range(coin_needed):
            change.append(coin)
            
        amount -= coin * coin_needed
        
    return change


"""
Rooks on a rampage - page 22
"""


def safe_squares_rooks(n, rooks):
    if len(rooks) < 1:
        return n * n
    
    dangerous_rows = []
    dangerous_cols = []
    safe_rows = []
    safe_cols = []
    
    for rook in rooks:
        dangerous_cols.append(rook[0])
        dangerous_rows.append(rook[1])
        
    safe_rows = get_available_number_in_range(list(set(dangerous_rows)), n)
    safe_cols = get_available_number_in_range(list(set(dangerous_cols)), n)
    
    #result is the product of the number of safe x positions and the number of safe y positions
    return len(safe_rows) * len(safe_cols)


def get_available_number_in_range(input_list, max_range):
    
    if len(input_list) == 0:
        return []
    
    input_list.sort()
    output_list = []
    output_list += [n for n in range(0, input_list[0])]
    
    for index, item in enumerate(input_list):
        if index < len(input_list) - 1:
            output_list += [n for n in range(item + 1, input_list[index + 1])]
        else:        
            output_list += [n for n in range(input_list[len(input_list) - 1] + 1, max_range)]
            
    return output_list


"""
Try a spatula - page 23
"""


def pancake_scramble(text):
    
    positions = [n for n in range(len(text))]
    for i in range(2, len(text) + 1):
        
        for index, position in enumerate(positions[:i][::-1]):
            positions[index] = position
            
    return ''.join([text[positions[i]] for i in range(len(positions))])


"""
Words with given shape - page 24
"""


def words_with_given_shape(words, shape):
    
    result = []
    for word in words:        
        if check_word_with_shape(word, shape):
            result.append(word)
            
    return result


def check_word_with_shape(word, shape):
    
    if len(word) != len(shape) + 1:
        return False
    
    for i in range(1, len(word)):
        
        if shape[i - 1] == -1:
            if word[i - 1] <= word[i]:
                return False
            
        if shape[i - 1] == 0:
            if word[i - 1] != word[i]:
                return False
            
        if shape[i - 1] == 1:
            if word[i - 1] >= word[i]:
                return False
            
    return True


"""
Chirality - page 25
"""

# not completed
def is_left_handed(pips):
    return


"""
The card that wins the trick - page 26
"""


def winning_card(cards, trump = None):
    
    rank = {'two': 1, 'three': 2, 'four': 3, 'five': 4, 'six': 5, 'seven': 6, 'eight': 7,
            'nine': 8, 'ten': 9, 'jack': 10, 'queen': 11, 'king': 12, 'ace': 13}
    
    potential_winning_hands = []
    
    # set trump as first card played IF
    # 1 - not already set
    # or
    # 2 - the set trump is not in the whole trick
    if not trump or not trump in [card[1] for card in cards]:
        trump = cards[0][1]
        
    for i in range(len(cards)):
        if cards[i][1] == trump:
            potential_winning_hands.append(cards[i])
            
    if len(potential_winning_hands) == 0:
        return cards[0]
    
    # sort the hands descending base on the ranks points
    potential_winning_hands.sort(key = lambda hand : rank[hand[0]], reverse = True)
    
    return potential_winning_hands[0]


"""
Do you reach many, do you reach one? - page 27
"""

# not completed
def knight_jump(knight, start, end):
    return


"""
Sevens rule, zeros drool - page 28
"""


def seven_zero(n):
    
    if has_only_seven_or_zero(n):
        return n
    
    # we check from length of number n if starting digit of n is lesser than 7
    # otherwise we check from length of number n + 1
    # e.g. n = 17, d = 2 so we're checking from 70, 77, .....
    # n = 81, d = 3 so we're checking from 700, 770, 777, .....
    d = len(str(n)) + (0 if str(n)[0] <= '7' else 1)
    
    while True:
        result = int('7' * d)
        if result % n == 0:
            return result
        
        k = 1
        while k < d:
            result = int('7' * k + '0' * (d - k))
            if result % n == 0:
                return result
            
            k += 1
            
        d += 1    
            
    
def has_only_seven_or_zero(n):
    
    for d in str(n):
        if d != '0' and d != '7':
            return False
        
    return True


"""
Fulcrum - page 29
"""


def can_balance(items):
    if len(items) == 1:
        return 0    
    
    # we first attempt to get the middle index of the list
    potential_fulcrum_index = len(items) // 2
    move_direction = get_balance_direction(potential_fulcrum_index, items)
    
    # if is balanced, return the fulcrum element index
    if move_direction == 0:
        return potential_fulcrum_index
    # if is not balanced and length is 3 or less
    if len(items) <= 3:
        return -1
    
    start_index, end_index, step = 0, 0, 0
    last_move_direction = 0
    offset = move_direction
    
    # if is left leaned, move to the left
    if move_direction < 0:
        start_index = potential_fulcrum_index - 1
        end_index = 0
        step = -1
        
    # if is right leaned, move to the right
    if move_direction > 0:
        start_index = potential_fulcrum_index + 1
        end_index = len(items) - 1
        step = 1
    
    # the algorithm to check all posible fulcrum indices until we reach a conclusion
    for i in range(start_index, end_index, step):
        
        # store moving direction
        last_move_direction = move_direction
        move_direction = get_balance_direction(potential_fulcrum_index + offset, items)
        
        # if current moving direction is the opposite of the last moving direction
        # meaning we went from posible fulcrum index to the heavier weight direction
        # then goes back toward the posible fulcrum index... meaning not possible to balance
        if last_move_direction * move_direction < 0:
            return -1
        
        if move_direction == 0:
            return potential_fulcrum_index + offset
        
        offset += move_direction


# check which side is heavier or if both are equals
# then get the moving direction to the heavier side to attempt balancing left and right
def get_balance_direction(potential_fulcrum_index, items):
    
    left_weight, right_weight = 0, 0
    
    for i in range(potential_fulcrum_index):
        left_weight += abs(i - potential_fulcrum_index) * items[i]
        
    for i in range(potential_fulcrum_index + 1, len(items)):
        right_weight += abs(i - potential_fulcrum_index) * items[i]
        
    # if balanced, don't move
    if left_weight == right_weight:
        return 0
    
    # if left heavy, move to left
    if left_weight > right_weight:
        return -1
    
    # if right heavy, move to right
    if left_weight < right_weight:
        return 1
    
    
"""
Fail while daring greatly - page 30
"""


def josephus(n, k):
    result = []
    count = 0
    # instantiate a list from 1 to n inclusively
    sample = [num for num in range(1, n + 1)]
    while len(sample) > 0:
        count = (count + k - 1) % len(sample)
        # takes out element at current count + k less 1
        # within the length of sample exclusively
        result.append(sample.pop(count))
    return result


"""
All your fractions are belong to base - page 31
"""


def group_and_skip(n, out, ins):
    
    coin_groups = n // out
    left_over = n % out
    left_over_list = [left_over]
    
    if coin_groups > 0:
        # call recursive function until n (= coin_groups * ins) is less or equal to 0
        left_over_list += group_and_skip(coin_groups * ins, out, ins)
        
    return left_over_list


"""
Count the balls off the brass monkey - page 32
"""


def pyramid_blocks(n, m, h):
    # WOLFRAM Sum[(n+i)(m+i), {i, 0, h-1}]
    return h * (1 - 3*h + 2*h*h - 3*m + 3*h*m - 3*n + 3*h*n + 6*m*n) // 6


"""
Count growlers - page 33
"""

def count_growlers(animals):
    facing_left = ['cat', 'dog']
    growler_count = 0
    
    # brute force solution... let's go for a better solution maybe??? (0.7s)
    # for i in range(len(animals)):
    #     is_facing_left = animals[i] in facing_left
    #     start_index = i + (1 if not is_facing_left else -1)
    #     end_index = -1 if is_facing_left else len(animals)
    #     step = -1 if is_facing_left else 1
    #     dog_cat_diff = 0
    #     for j in range(start_index, end_index, step):
    #         dog_cat_diff += 1 if animals[j] in dogs else -1
    #     growler_count += 1 if dog_cat_diff > 0 else 0
            
    # attempting for a faster solution (0.1s)
    dogs_to_the_right = count_dogs(animals, len(animals) - 2, -1, -1)
    dogs_to_the_left = count_dogs(animals, 1, len(animals), 1)
    
    for i in range(len(animals)):
        is_facing_left = animals[i] in facing_left
        dog_cat_diff = dogs_to_the_left[i] if is_facing_left else dogs_to_the_right[i]
        growler_count += 1 if dog_cat_diff > 0 else 0
        
    return growler_count

# count dogs to the right or left of every elements in the current animals list
def count_dogs(animals, start_index, end_index, step):
    
    dogs, dog_counts = ['dog', 'god'], [0]
    dog_count = 0
    
    for i in range(start_index, end_index, step):
        dog_count += 1 if animals[i + -step] in dogs else -1
        
        if step == -1:
            dog_counts.insert(0, dog_count)
            
        elif step == 1:
            dog_counts.append(dog_count)
            
    return dog_counts


"""
Bulgarian solitaire - page 34
"""


def bulgarian_solitaire(piles, k):
    
    goal = [n for n in range(1, k + 1)]
    
    piles.sort()
    
    count = 0
    
    while piles != goal:
        count += 1
        
        # a list of zero element indices
        zero_elements_indices = []
        new_pile = 0
        
        # the bulgarian solitaire playing rules
        for i in range(len(piles)):
            piles[i] -= 1
            new_pile += 1
            
            if piles[i] == 0:
                zero_elements_indices.append(i - len(zero_elements_indices))
                
        # remove all zeroes if available
        if len(zero_elements_indices) > 0:
            for index in zero_elements_indices:
                del piles[index]
                
        piles.append(new_pile)
        piles.sort()
        
    return count


"""
Scylla or Charybdis? - page 35
"""

# not completed
def scylla_or_charybdis(moves, n):
    return


def get_step_direction_sum(seq, step = 1):
    return sum([1 if seq[i] == '+' else -1 for i in range(0, len(seq), step)])


def get_safe_squares(n):
    return 2 * (n - 1) + 1

# arguments = [
#     { 
#         'moves':'-++--++-++++',
#         'n'    :2,
#         'k'    :3
#     },
#     { 
#         'moves':'--++++---+-++-+++++++++++',
#         'n'    :5,
#         'k'    :5
#     },
#     { 
#         'moves':'+-++---+-+-++-+++----+++-++-+---+--++++++++++',
#         'n'    :5,
#         'k'    :7
#     },
#     { 
#         'moves':'+--++---+-++-+++------+++++---++-+--+++-+--++-++-++-+-++++++++++++++++++',
#         'n'    :9,
#         'k'    :1
#     }
# ]
# for argument in arguments:
#     print('direction:', get_step_direction_sum(argument['moves']))
#     print('length:   ', len(argument['moves']))
#     print('safe spot:', get_safe_squares(argument['n']), '\n')
#     print()



                                #        n = 9
                                #      12345678 <-- n - 1
                                #     0       |
                                #      +      |
                                #    --       |
                                #     ++      |
                                #   ---       |
                                #    +        |
                                #   -         |
                                #    ++       |
                                #    -        |
                                #     +++     |
                                # ------      |
                                #  +++++      |
                                #   --        |
                                #    ++       |
                                #    -        |
                                #     +       |
                                #   --        |
                                #    +++      |
                                #     -       |
                                #      +      |
                                #    --       |
                                #     ++      |
                                #     -       |
                                #      ++     |
                                #      -      |
                                #       ++    |
                                #       -     |
                                #        +    |
                                #       -     |left over = 12
                                #        +++++|++++++++++++

"""
Longest arithmetic progression - page 36
"""

# not completed
def arithmetic_progression(items, stride = None):
    # start = items[0]
    # stride = 0
    # n = 1
    
    # if len(items) <= 1:
    #     return (start, stride, n)
    
    # whole = [a for a in range(0, items[len(items) - 1])]
    # print(whole)
    # for i in range(len(items) - 1):
    #     stride = items[i + 1] - items[i]
    #     for j in range(i, len(items) - 1):
    #         if items[j] + stride == items[j + 1]:
    #             n += 1
    #         else:
    #             n = 1
    #             break
    # return (start, stride, n)
    
    
    if len(items) <= 1:
        return (items[0], 0, 1)
    
    start = 0
    if stride == None:
        stride = 0
    prog_seq = []
    # n = 0
    index_stride_dict = {}
    
    for i in range(len(items) - 1):
        index_stride_dict[items[i]] = items[i + 1] - items[i]
    
    i = 0
    j = 1
    while i < len(items) - j:
        # start and stride don't change when
        # process 1 success
        index_to_check = i + j
        start = items[i]
        stride = items[index_to_check] - start
        prog_seq.append(start)
        prog_seq.append(items[index_to_check])
        
        # process 1
        while j < len(items) - i:
            k = j + 1
            index_to_check = k + 1
            while k < len(items) - index_to_check:
                # print(f'i {i} - j {j} - k {k}')
                # print(f'index_to_check = {index_to_check}')
                if items[index_to_check] + stride == items[index_to_check + k]:
                    prog_seq.append(items[index_to_check])
                    index_to_check = k
                    break
                k += 1
            j += 1
            if j == len(items) - i:
                j = 0
                break
        i += 1
                
    # return (start, stride, n)
    return prog_seq
                
# print(arithmetic_progression([2, 4, 5, 6, 8, 12, 17]))
    
    
    
    
    
# def my_func(items, i = None, j = None):
#     if i == None:
#         i = 0
#     if j == None:
#         j = 1
#     if i < len(items) - j:
#         if j < len(items) - i:
#             if items[i] + stride == items[i + j]:
#                 prog_seq.append(items[j])
#             else:
#                 # do something
#             j += 1
#             if j == len(items) - i:
#                 j = 1
#                 break
#         i += 1
    
        
#     return index_stride_dict




# print(my_func(range(100)))
    
# def test_al(items_arr) :
#     stride_count = 0
#     stride = 0
    
#     while stride_count < len(items_arr) - 1:
#         sequence_found = []
#         stride = items_arr[stride_count + 1] - items_arr[stride_count]
#         start = items_arr[stride_count]
#         sequence_found.append(start)
#         index = stride_count + 1
#         while index < len(items_arr):
#             if (items_arr[index] - start) / stride == 0:
#                 sequence_found.append(items_arr[index])
#             index += 1
#         stride_count += 1
      
#         print(sequence_found)

  # tuple result is (start, stride, len(sequence_found)

    
# print(test_al([2, 4, 6, 7, 8, 12, 17]))


# print(arithmetic_progression([2, 4, 6, 7, 8, 12, 17]))


"""
Best one out of three - page 37
"""

# not completed
def tukeys_ninthers(items):
    res = []
    for i in range(0, len(items), 3):
        res.append(sum(items[i:i+4]) // 3)
    if len(res) > 1:
        return tukeys_ninthers(res)
    return res


"""
Collecting numbers - page 38
"""


def collect_numbers(perm):
    
    inv_perm = get_inverted_permutation(perm)
    count = 1
    
    for i in range(len(inv_perm) - 1):
        if inv_perm[i] > inv_perm[i + 1]:
            count += 1
            
    return count


"""
Between the soft and the NP-hard place - page 39
"""


# NEED TO FIX PDF DESCRIPTION!!!!!!!!!
def verify_betweenness(perm, constraints):
    
    for constraint in constraints:
        if not find_match(perm, constraint) and not find_match(perm[::-1], constraint):
            return False
        
    return True


def find_match(perm, constraint):
    
    match_found = 0
    match_index = -1
    
    for i in range(len(constraint)):
        for j in range(match_index + 1, len(perm)):
            if constraint[i] == perm[j]:
                match_index = j
                match_found += 1
                break
            
    return match_found == len(constraint)


"""
Count Troikanoff, I presume - page 40
"""


def count_troikas(items):
    
    element_frequency_dict = get_element_index_dict(items)
    
    # print(element_frequency_dict)
    
    troikas = 0
    
    for key in element_frequency_dict.keys():
        
        if len(element_frequency_dict[key]) < 3:
            #print(f'continue here because element_frequency_dict[{key}] {element_frequency_dict[key]} < 3')
            continue
        
        #print('\nbegins checking for troikas')
        for outer_index in range(len(element_frequency_dict[key]) - 2):
        
            i = element_frequency_dict[key][outer_index]
            
            #print(f'i = {i}')
            for inner_index in range(outer_index + 1, len(element_frequency_dict[key]) - 1):
            
                j = element_frequency_dict[key][inner_index]
                #print(f'\tj = {j}')
                k = 2 * j - i
                #print(f'\tk = {k}')
                
                if k not in range(len(items)):
                    #print(f'break here because k {k} is not in range of items {len(items)}')
                    break
                
                if items[i] == items[j] == items[k]:
                    #print(f'troika found at i {i}, j {j}, k {k}')
                    troikas += 1
                    
    return troikas


"""
Crack the crag - page 41
"""


def has_pair(dice):
    for i in range(len(dice) - 1):
        for j in range(i + 1, len(dice)):
            if dice[i] == dice[j]:
                return True
    return False


def has_three(dice):
    for i in range(len(dice) - 1):
        if dice[i] != dice[i + 1]:
            return False
    return True


# check for straight and also whether they are
# low-high straight (123, 456) or odd-even straight (135, 246)
# SORTED SEQUENCE ONLY!!!
def is_valid_straight(dice):
    # Combined
    # i, j, k = 0, 1, 2
    # is_straight = dice[k] - dice[j] == dice[j] - dice[i]
    # is_low_high_straight = is_straight and dice[j] - dice[i] == 1 and (dice[i] == 1 or dice[i] == 4)
    # is_odd_even_straight = is_straight and dice[j] - dice[i] == 2
    # return is_low_high_straight or is_odd_even_straight
    
    # Splitted
    low_straight = is_low_straight(dice)
    high_straight = is_high_straight(dice)
    odd_straight = is_odd_straight(dice)
    even_straight = is_even_straight(dice)
    return low_straight or high_straight or odd_straight or even_straight


def is_straight(dice):
    i, j, k = 0, 1, 2
    return dice[k] - dice[j] == dice[j] - dice[i]


def is_consecutive_straight(dice):
    return is_straight(dice) and dice[1] - dice[0] == 1


def is_low_straight(dice):
    return is_consecutive_straight(dice) and dice[0] == 1


def is_high_straight(dice):
    return is_consecutive_straight(dice) and dice[0] == 4


def is_skip_straight(dice):
    return is_straight(dice) and dice[1] - dice[0] == 2


def is_odd_straight(dice):
    return is_skip_straight(dice) and dice[0] == 1


def is_even_straight(dice):
    return is_skip_straight(dice) and dice[0] == 2
    

def get_category(dice):
    # ascending sort
    dice.sort()
    
    category = -1
    
    # check for crag (thirteen with pair) or thirteen
    if sum(dice) == 13:
        # check pair
        if has_pair(dice):
            category = 0        #---- CRAG
        else:
            category = 1        #---- THIRTEEN
    elif has_three(dice):
        category = 2            #---- THREE OF A KIND
    elif is_valid_straight(dice):
        category = 3            #---- STRAIGHT (LOW-HIGH-ODD-EVEN)
    else:
        category = 4            #---- ANY NUMBERS (ONES - SIXES)
    
    return category


# multiply the face value with its occurences
# then return the highest score possible
def get_any_numbers_score(dice):
    
    dice_frequency_dict = {}
    
    for i in range(len(dice)):
        if dice[i] not in dice_frequency_dict:
            dice_frequency_dict[dice[i]] = 1
            
        else:
            dice_frequency_dict[dice[i]] += 1
            
    return max(entry[0] * entry[1] for entry in dice_frequency_dict.items())


def crag_score(dice):
    
    constant_scoring_categories = { 0 : 50, 1 : 26, 2 : 25, 3 : 20 }
    
    category = get_category(dice)
    
    if category < 4:
        return constant_scoring_categories[category]
    
    return get_any_numbers_score(dice)


"""
Three summers ago - page 42
"""


def three_summers(items, goal):
    
    for i in range(len(items)):
        new_items = get_list_without_element_at_index(items, i)
        if two_summers(new_items, goal - items[i]):
            return True
        
    return False


def two_summers(items, goal, i = 0, j = None):
    
    if j == None:
        j = len(items) - 1    
        
    if i < j:
        
        if items[i] + items[j] > goal:
            return two_summers(items, goal, i, j - 1)
        
        if items[i] + items[j] < goal:
            return two_summers(items, goal, i + 1, j)
        
        if items[i] + items[j] == goal:
            return (i, j)
        
    return None


"""
Sum of two squares - page 43
"""


def sum_of_two_squares(n):
    
    i, j = 1, int(numpy.sqrt(n - 1))
    
    while i <= j:
        
        if i * i + j * j < n:
            i += 1
            
        elif i * i + j * j > n:
            j -= 1
            
        else:
            return (j, i)
        
    return None


"""
Carry on Pythonista - page 44
"""

def count_carries(a, b, print_result = False):
    
    # initial values
    carry_count, carry_over = 0, 0
    
    # convert a and b to string for interation
    a_str, b_str = str(a), str(b)
    
    smaller_number = a_str if a <= b else b_str
    bigger_number = a_str if a > b else b_str
    
    # used to calculate the index for smaller number
    len_diff = len(bigger_number) - len(smaller_number)
    
    # 99999999 -> length of 8 starts at index_1 = 7
    # 88       -> length of 2 starts at index_2 = 1 or index_1 - length difference = 7 - 6 = 1
    # length difference   = 6
    
    # it's a bit harder to calculate index if we choose to iterate backward
    for i in range(len(bigger_number) - 1, -1, -1):
        
        sum_digit = 0
        
        # if i - len_diff >= 0 meaning we have digits to add between 2 numbers
        if i >= len_diff:
            sum_digit = int(smaller_number[i - len_diff]) + int(bigger_number[i]) + carry_over
        else:
            # break if we run out of digits from smaller number AND carry over is 0 or less
            if carry_over <= 0: break
            
            sum_digit = int(bigger_number[i]) + carry_over
        
        # after we have used the carry over, we set it to 0
        carry_over = 0
        
        if sum_digit > 9:
            # get the tens and assign to carry over
            carry_over = sum_digit // 10
            
            carry_count += 1
    
    return carry_count


"""
As below, so above - page 45
"""

# not completed
def leibniz(heads, positions):
    return


"""
Expand positive integer intervals - page 46
"""


def expand_intervals(intervals):
    
    # handle ''
    if intervals == '':
        return []
    
    result = []
    
    # handle comma separated intervals
    intervals_list = intervals.split(',')
    for i in range(len(intervals_list)):
        
        # handle dash separated intervals
        # returns original string if there is no dash
        # meaning '42'.split('-') -> '42'
        limits = intervals_list[i].split('-')
        
        # add to result if only one limit
        if len(limits) == 1:
            result.append(int(limits[0]))
            
        # otherwise add to the result a list from lower limit to upper limit inclusively
        else:
            result += [n for n in range(int(limits[0]), int(limits[1]) + 1)]
            
    return result


"""
Collapse positive integer intervals - page 47
"""


def collapse_intervals(items):
    # handles []
    if items == []:
        return ''
    
    sublists = {1:[items[0]]}
    
    # find consecutive sublists
    sublist_count = 1
    for i in range(len(items) - 1):
        
        # if is consecutive, add to list
        if items[i + 1] - items[i] == 1:
            sublists[sublist_count].append(items[i + 1])
        
        # otherwise 
        else:
            sublist_count += 1
            sublists[sublist_count] = [items[i + 1]]
            
    return ','.join([str(v[0]) if len(v) == 1 else f'{v[0]}-{v[len(v) - 1]}' for k, v in sublists.items()])


"""
Prominently featured - page 48
"""


class Peak():
    def __init__(self, position = 0, height = 0, prominence = 0):
        self.position = position
        self.height = height
        self.prominence = prominence
    
    def get_info(self):
        return (self.position, self.height, self.prominence)
    
# returns all the peaks in the given heights list
# a height is a peak when its value is
# HIGHER than its IMMEDIATE left and/or right values
def find_peaks(heights):
    if len(heights) < 3:
        return [max(heights)]
    
    peaks = []
    
    for i in range(1, len(heights) - 1):
        # left edge check
        if i == 1 and heights[i] < heights[i - 1]:
            peaks.append(Peak(i - 1, heights[i - 1], 0))
            
        # right edge check
        if i == len(heights) - 2 and heights[i] < heights[i + 1]:
            peaks.append(Peak(i + 1, heights[i + 1], 0))
        
        # middle cases
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            peaks.append(Peak(i, heights[i], 0))
    
    return peaks

# returns the lowest and 
def find_lo_hi_height(current_peak, heights, start_pos, end_pos, step):
    
    lowest_height = None
    highest_height = None
    current_peak_pos = current_peak.position
    
    for i in range(start_pos, end_pos + step, step):
        if (step == -1 and i < current_peak_pos) or (step == 1 and i > current_peak_pos):
            
            highest_height = heights[i] if highest_height == None else max(highest_height, heights[i])
            lowest_height = heights[i] if lowest_height == None else min(lowest_height, heights[i])
                    
            if current_peak.height < heights[i]:
                break
        
    return [lowest_height, highest_height]


def prominences(heights):
    # print(heights)
    
    max_height = max(heights)
    
    # handles input with 1 or 2 peaks lists
    if len(heights) < 3:
        if max_height == 0:
            return []
        return [(heights.index(max_height), max_height, max_height)]
    
    peaks = find_peaks(heights)
    
    for current_peak in peaks:
        # run from current peak to right
        right_lo_hi = find_lo_hi_height(current_peak, heights, current_peak.position, peaks[len(peaks) - 1].position, 1)
    
        # run from current peak to left
        left_lo_hi = find_lo_hi_height(current_peak, heights, current_peak.position, peaks[0].position, -1)
        
        # prominence is the height itself if peak is highest
        if current_peak.height == max_height:
            current_peak.prominence = max_height
            continue
        
        '''
        ########## skip below steps if current peak is highest ##########
        '''
        
        # if reach here, we can safely assume that current peak is not highest
        # check if current peak is LEFT edge meaning there is no other peak to its LEFT
        # prominence is the descent to the LOWEST valley to its RIGHT before meeting HIGHER peak
        if left_lo_hi[1] == None:
            current_peak.prominence = current_peak.height - right_lo_hi[0]
            continue
        
        '''
        ########## skip below steps if current peak left edge ##########
        '''
        
        # if reach here, we can safely assume that current peak is not left edge
        # check if current peak is RIGHT edge meaning there is no other peak to its RIGHT
        # prominence is the descent to the LOWEST valley to its LEFT before meeting HIGHER peak
        if right_lo_hi[1] == None:
            current_peak.prominence = current_peak.height - left_lo_hi[0]
            continue
        
        '''
        ########## skip below steps if current peak is right edge ##########
        '''
        
        # if reach here, we can safely assume that current peak is not left edge
        # if middle peak meaning current peak is in the middle of 2 other LEFT and RIGHT peaks
        # prominence can be calculated under one of two cases
        # 1 - if current peak is LOWER than BOTH peaks on its LEFT AND RIGHT
        # prominence is the descent to the HIGHEST valley to its LEFT or RIGHT
        # 2 - if current peak is HIGHER than EITHER peak on its LEFT OR RIGHT
        # prominence is the descent to the LOWEST valley to the HIGHER peak
        if left_lo_hi[1] > 0 and right_lo_hi[1] > 0:
            
            is_smaller_than_left = left_lo_hi[1] > current_peak.height
            is_smaller_than_right = right_lo_hi[1] > current_peak.height
            
            if is_smaller_than_left and is_smaller_than_right:
                current_peak.prominence = current_peak.height - max(left_lo_hi[0], right_lo_hi[0])
            elif is_smaller_than_left:
                current_peak.prominence = current_peak.height - left_lo_hi[0]
            elif is_smaller_than_right:
                current_peak.prominence = current_peak.height - right_lo_hi[0]
            else:
                # SHOULD NOT REACH HERE...
                print('Something is seriously wrong!!!')
    
    return [peak.get_info() for peak in peaks]


"""
Like a kid in a candy store, except without money - page 49
"""


def has_element_larger_than_one(l):
    for e in l:
        if e > 1:
            return True
    return False


def candy_share(candies):
    
    candies_len = len(candies)
    add_right = [0] * candies_len
    add_left = [0] * candies_len
    count = 0
    
    # fail safe
    max_cycle = 100000
    
    while has_element_larger_than_one(candies):
        
        for i in range(candies_len):
            if candies[i] > 1:
                candies[i] -= 2
                add_right[(i + 1) % candies_len] += 1
                add_left[(i - 1) % candies_len] += 1
                
        for i in range(candies_len):
            candies[i] += add_right[i] + add_left[i]
            add_right[i] = add_left[i] = 0
            
        count += 1
        
        max_cycle -= 1
        # fail safe
        if max_cycle <= 0:
            print('max cycle reached... breaking out of loop')
            break
        
    # return candies
    return count


"""
Dibs to dubs - page 50
"""


def duplicate_digit_bonus(number):
    
    # handles numbers less than 10
    if number // 10 == 0:
        return 0
    
    duplicate_numbers = get_duplicate_numbers(number)
    score = 0
    
    for dup_num in duplicate_numbers:
        score += calculate_score(dup_num)
    
    # bonus score if ends with duplicate numbers
    if len(duplicate_numbers) > 0:
        last_duplicate_number = duplicate_numbers[len(duplicate_numbers) - 1]
            
        if str(number).endswith(last_duplicate_number):
            score += calculate_score(last_duplicate_number)
    
    return score


def calculate_score(duplicate_number):
    return 10 ** (len(duplicate_number) - 2)


"""
Nearest smaller element - page 51
"""


def nearest_smaller(items):
    
    smallest = min(items)
    result = [0] * len(items)
    
    for i in range(len(items)):
        
        # if already smallest, take the value
        if items[i] == smallest:
            result[i] = smallest
            
        else:
            # get indices of smaller nearest elements on the left and right of current item
            # will return None if there is no smaller element on that direction
            left_nearest_smaller_index = get_index_of_nearest_smaller(items, i, -1, -1)
            right_nearest_smaller_index = get_index_of_nearest_smaller(items, i, len(items), 1)
            
            # get the distance difference between the indices found above and the index of current item
            left_index_diff = get_index_difference(i, left_nearest_smaller_index)
            right_index_diff = get_index_difference(i, right_nearest_smaller_index)
            
            # get closest smaller element
            if right_index_diff != None and (left_index_diff == None or left_index_diff > right_index_diff):
                result[i] = items[right_nearest_smaller_index]
                continue
            
            if left_index_diff != None and (right_index_diff == None or left_index_diff < right_index_diff):
                result[i] = items[left_nearest_smaller_index]
                continue
            
            if left_index_diff != None and right_index_diff != None:
                min_value = custom_min(items[left_nearest_smaller_index], items[right_nearest_smaller_index])
                result[i] = min_value
        
    return result


def get_index_of_nearest_smaller(items, start, end, step):
    for i in range(start, end, step):
        if items[start] > items[i]:
            return i
    return None


def get_index_difference(i, j):
    if i != None and j != None:
        return abs(i - j)
    return None
        
        
def custom_min(*args):
    l = []
    for arg in args:
        if arg != None:
            l.append(arg)
    if len(l) < 1: return None
    return min(l) if len(l) > 1 else l[0]


"""
Interesting, intersecting - page 52
"""


def squares_intersect(s1, s2):
    # we have square1 (x1, y1, length_1) and square2 (x2, y2, length_2)
    # let's say square1 is on the left of square2 meaning x1 < x2
    # and square2 is on the bottom of square1 meaning y2 < y1
    # they are intersected when x1 + length_1 >= x2 AND y2 + length_2 >= y1
    # in short, x_left + length_left >= x_right AND y_bottom + length_bottom >= y_top
    
    # we first find the square on the left, right, top, and bottom
    left, right = s1 if s1[0] < s2[0] else s2, s1 if s1[0] > s2[0] else s2
    bottom, top = s1 if s1[1] < s2[1] else s2, s1 if s1[1] > s2[1] else s2
    
    # apply logic x_left + length_left >= x_right AND y_bottom + length_bottom >= y_top
    return left[0] + left[2] >= right[0] and bottom[1] + bottom[2] >= top[1]


"""
So shall you sow - page 53
"""


def oware_move(board, house_index):
    
    seeds_to_sow = board[house_index]
    
    # set the house we took the seeds from to 0
    board[house_index] = 0
    
    stop_sowing_house_index = -1
    
    # if we have enough seeds to loop the board more than once
    # we check if seeds_to_sow >= len(board) because we skip sowing
    # at the house we picked up the seeds from
    # meaning if board has 8 houses, and we picked up 7
    # we can sow up to the house just before the house we picked up the seeds from
    # and if we picked up 8 seed, we skip the house where the seeds was from
    # and sow up to the house next to the house we picked up the seeds from
    # therefore, we need at least len(board) number of seeds to loop the board more than once
    if seeds_to_sow >= len(board):
        
        seeds_per_house = seeds_to_sow // (len(board) - 1) # skip origin house so it's len(board) - 1
                                                            # evenly distributed seeds per house if can loop the board more than once
                                                           
        seeds_left_over = seeds_to_sow % (len(board) - 1)  # we will have left over if we loop the board more than once
        
        # sow the seeds
        for i in range(len(board)):
            if i == house_index: continue # skip origin house
            board[i] += seeds_per_house
        
        
        # sow the left over seeds after looping
        for i in range(seeds_left_over):
            board[(house_index + i + 1) % len(board)] += 1 # sow from the house next to the origin house
                                                           # and wrap over if index goes out of bound up to origin house index - 1
                                                           # because left over seeds is not enough to loop the board
                                                           
        # we keep track of the house index that we stop sowing
        stop_sowing_house_index = (house_index - 1 + seeds_left_over if seeds_left_over == 0 else house_index + seeds_left_over) % len(board)
    
    # if we don't need to loop the board
    else:
        
        # sow the seeds
        for i in range(seeds_to_sow):
            board[(house_index + i + 1) % len(board)] += 1
            
        stop_sowing_house_index = (house_index + seeds_to_sow) % len(board)
        
    return capture_seeds(board, stop_sowing_house_index)
    seeds_to_sow = board[house_index]
    
    seeds_per_house = seeds_to_sow // (len(board) - 1) # skip origin house so it's len(board) - 1
                                                       # evenly distributed seeds per house if can loop the board more than once
                                                       
    seeds_left_over = seeds_to_sow % (len(board) - 1)  # we will have left over if we loop the board more than once
    
    # sow the seeds
    for i in range(len(board)):
        if i == house_index: continue # skip origin house
        board[i] += seeds_per_house
    
    

    stop_sowing_house_index = -1
    
    if seeds_to_sow >= len(board):
        
        # sow the left over seeds after looping
        for i in range(seeds_left_over):
            board[(house_index + i + 1) % len(board)] += 1 # sow from the house next to the origin house
                                                           # and wrap over if index goes out of bound up to origin house index - 1
                                                           # because left over seeds is not enough to loop the board
                                                           
        stop_sowing_house_index = (house_index - 1 + seeds_left_over if seeds_left_over == 0 else house_index + seeds_left_over) % len(board)
        
    else:        
        
        stop_sowing_house_index = (house_index + seeds_to_sow) % len(board)                                      
                                                       
    return (board, stop_sowing_house_index)


def capture_seeds(board, stop_sowing_house_index):
    
    # remove from the house we stopped sowing from if it's in opponent's territory
    is_in_opponent_territory = stop_sowing_house_index >= len(board) // 2
    
    if is_in_opponent_territory:
        
        for i in range(stop_sowing_house_index, len(board) // 2 - 1, -1):
            
            # continue to take seeds from opponent if satisfy condition
            if board[i] == 2 or board[i] == 3:
                board[i] = 0
                
            # stop when we cannot take the seeds
            else: break
        
    return board


"""
That's enough of you! - page 54
"""


def remove_after_kth(items, k=1):
    
    seen = get_element_frequency_dict(items)
    
    for i in range(len(items) - 1, -1, -1):
        if seen[items[i]] > k:
            seen[items[i]] -= 1
            items[i] = None
            
    return remove_element_with_value(items, None)


"""
Brussel's choice - page 55
"""


def brussels_choice_step(n, mink, maxk):
    
    result = []
    
    for k in range(mink, maxk + 1):
        result += brussels_substring_transform(str(n), k)
        
    result.sort()
    
    return result


def brussels_substring_transform(number_string, number_count):
    
    brussels_substrings = []
    
    for i in range(len(str(number_string)) - number_count + 1):
        # first part
        sub_n_str_pre = number_string[ : i ]
        # mid part
        sub_n_str_mid = number_string[ i : i + number_count ]
        # last part
        sub_n_str_pst = number_string[ i + number_count : ]
        
        # the part that we need to calculate is mid
        sub_n_int = int(sub_n_str_mid)
        
        if sub_n_int % 2 == 0:
            brussels_substrings.append(int(sub_n_str_pre + str(sub_n_int // 2) + sub_n_str_pst))
            
        brussels_substrings.append(int(sub_n_str_pre + str(sub_n_int * 2) + sub_n_str_pst))
        
    return brussels_substrings


"""
Cornered cases - page 56
"""

# not completed
def count_corners(points):
    
    # condition to be corner:
    # p1 (x, y + h)
    #     |\
    #     |  \
    #     |    \
    #     |      \
    #     |        \
    #     |__________\
    # p0 (x, y)     p2 (x + h, y)
    
    count = 0
    
    tris = []
    
    same_x = {}
    same_y = {}
    
    for point in points:
        if point[0] not in same_x:
            same_x[point[0]] = [point[1]]
        else:
            same_x[point[0]].append(point[1])
            
        if point[1] not in same_y:
            same_y[point[1]] = [point[0]]
        else:
            same_y[point[1]].append(point[0])
            
    print('same x', same_x)
    print('same y', same_y)
    
    for x in same_x:
        for y in same_x[x]:
            print(f'{x}, {y}')
            
    return tris


# print(count_corners([(1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (3, 3), (4, 3)]))


"""
Count consecutive summers - page 57
"""

# what???... wow...
# by definition, the count of consecutive number that adds up to the number n
# is the count of the odd divisors + 1
def count_consecutive_summers(n):
    count = 1
    for i in range(2, n + 1):
        # if is odd divisor
        if i % 2 == 1 and n % i == 0:
            count += 1
    return count


"""
McCulloch's second machine - page 58
"""


def mcculloch(digits):
    
    command_dict = {
        '3' : lambda y : y + '2' + y,
        '4' : lambda y : y[ : : -1 ],
        '5' : lambda y : y + y 
    }
    
    # the first '2' is the break number between
    # the commands and the part we need to work on which is y
    break_index = digits.index('2')
    
    y = digits[ break_index + 1 : ]
    commands = digits[ : break_index ]
    
    for command in command_dict['4'](commands):
        y = command_dict[command](y)
        
    return y


"""
That's enough for you! - page 59
"""


def first_preceded_by_smaller(items, k = 1):
    
    # iterate from index = k because we don't need to
    # check an item that has no k elements before it
    # Ex: [1, 2, 3, 4, 5], k = 3, we check from 4 onward
    for i in range(k, len(items)):
        
        smaller_count = 0
        
        # from 0 to i, keep track of the elements
        # that are smaller than the current element
        for j in range(i):
            
            if items[j] < items[i]:
                smaller_count += 1
            
            # we have a hit if the count is equals to k
            # don't need to check further since the number
            # of smaller elements preceeded current elements
            # don't need to be exactly equal to k
            if smaller_count == k:
                return items[i]
    
    return None


"""
Crab bucket list - page 60
"""

# line 2587 in tester109
def eliminate_neighbours(items):
    
    # handles length 1
    if len(items) < 2:
        return 1
    
    index_nodes = []
    element_dict = {}
    current_smallest_item = 1
    largest_item = max(items)
    largest_seen = 1
    count = 0
    
    # populate index nodes and 
    for i in range(len(items)):
        left_index = i - 1 if i - 1 >= 0 else None
        left_node = index_nodes[ left_index ] if left_index != None else None
        curr_node = Node( items[i] )
        curr_node.left_node = left_node
        
        if left_node != None:
            left_node.right_node = curr_node
            
        index_nodes.append( curr_node )
        
        element_dict[ items[ i ] ] = {'index': i, 'seen': False}
        
    while largest_seen != largest_item:
        
        # remove biggest neighbor node
        current_smallest_item_node = index_nodes[ element_dict[ current_smallest_item ][ 'index' ] ]
        
        left_node = current_smallest_item_node. left_node
        
        right_node = current_smallest_item_node. right_node
        
        biggest_neighbor_node = None
        
        if not left_node:
            biggest_neighbor_node = right_node
            
        elif not right_node:
            biggest_neighbor_node = left_node
            
        else:
            biggest_neighbor_node = left_node if left_node. data > right_node. data else right_node
            # biggest_neighbor_node = left_node if left_node > right_node else right_node
        
        if biggest_neighbor_node:
            largest_seen = biggest_neighbor_node. data
            element_dict[ largest_seen ][ 'seen' ] = True
            remove_node( biggest_neighbor_node )
        
        # remove current smallest item
        element_dict[ current_smallest_item ][ 'seen' ] = True
        remove_node( current_smallest_item_node )
        
        count += 1
        
        if current_smallest_item == largest_item:
            break
        
        while current_smallest_item < largest_item and element_dict[ current_smallest_item ][ 'seen' ] == True:
            current_smallest_item += 1
        
    return count


def remove_node(curr_node):
    if curr_node:
    
        left_node = curr_node.left_node
        
        right_node = curr_node.right_node
        
        # if there is a left node
        # set the right node of that left node
        # to be the right node of current node
        if left_node:
            left_node.right_node = right_node
        
        # if there is a right node
        # set the left node of that right node
        # to be the left node of current node
        if right_node:
            right_node.left_node = left_node
        
        # now we remove the connection of the
        # current node to its left and right nodes
        curr_node.left_node = None
        curr_node.right_node = None


# line 2588 in tester109
# def eliminate_neighbours(items):
    
#     # handles length 1
#     if len(items) < 2:
#         return 1
    
#     item_value_nodes = DoublyLinkedList()
#     # index_nodes = []
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


"""
What do you hear, what do you say? - page 61
"""


def count_and_say(digits):
    return ''.join([str(len(distinct_digit_block)) + distinct_digit_block[0] for distinct_digit_block in get_distinct_numbers(digits)])


"""
Bishops on a binge - page 62
"""

# not completed
def safe_squares_bishops(n, bishops):
    return


"""
Dem’s some mighty tall words, pardner - page 63
"""

# not completed
def word_height(words, word):

    for i in range(1, len(word)):
        
        left_word = word[:i]
        left_word_index = bisect.bisect_left(words, left_word)
        right_word = word[i:]
        right_word_index = bisect.bisect_left(words, right_word)
        
        if left_word == words[left_word_index] and right_word == words[right_word_index]:
            
            left_height = word_height(words, left_word)
            right_height = word_height(words, right_word)
            
            height = max(left_height, right_height) + 1
            
            return height
    
    word_index = bisect.bisect_left(words, word)
    if word == words[word_index]:
        height = 1
        return height
    else:
        height = 0
        return height
    
    return None


"""
Up for the count - page 64
"""

# not completed
get_number_of_digit = lambda lower_bound, upper_bound, power : (upper_bound - lower_bound) * power


def counting_series(n):
    #                                                                                       This is where index n is in
    #                                                                                                   |
    #     lower            upper                                                    power               |
    #       |                |                                                        |                 |
    #       v                v                                                        v                 v
    # range(         1   -            10)             -> 9 numbers            -> 9   * 1     digits =           9 digits
    # range(        10   -           100)            -> 90 numbers           -> 90   * 2     digits =         180 digits
    # range(       100   -          1000)           -> 900 numbers          -> 900   * 3     digits =        2700 digits
    # range(      1000   -         10000)          -> 9000 numbers         -> 9000   * 4     digits =       36000 digits
    # range(     10000   -        100000)         -> 90000 numbers        -> 90000   * 5     digits =      450000 digits
    # range(    100000   -       1000000)        -> 900000 numbers       -> 900000   * 6     digits =     5400000 digits
    # range(   1000000   -      10000000)       -> 9000000 numbers      -> 9000000   * 7     digits =    63000000 digits
    # range(  10000000   -     100000000)      -> 90000000 numbers     -> 90000000   * 8     digits =   720000000 digits
    # range( 100000000   -    1000000000)     -> 900000000 numbers    -> 900000000   * 9     digits =  8100000000 digits
    # range(1000000000   -   10000000000)    -> 9000000000 numbers   -> 9000000000   * 10    digits = 90000000000 digits
    
    total_digits = 0
    power = 0
    lower_bound, upper_bound = 0, 0
    num_of_digit_lower, num_of_digit_upper = 0, 0
    
    while num_of_digit_upper < n:
        power += 1
        lower_bound = 10 ** power
        upper_bound = 10 ** (power + 1)
        num_of_digit_lower = get_number_of_digit(lower_bound // 10, upper_bound // 10, power)
        num_of_digit_upper = get_number_of_digit(lower_bound, upper_bound, power + 1)
        
        total_digits += num_of_digit_lower
    
    num_count = (n - total_digits) // power
    
    # number of digits = (upper - lower) * power
    # e = (10 ^ (p + 1) - 10 ^ p) * p
    
    # print(f'index {n} belongs to number in range {lower_bound} - {upper_bound}')
    # print(f'{num_of_digit_lower} - {num_of_digit_upper}')
    # print(f'num_count with power {power}: {num_count}')
    # print(f'total_digits below n {total_digits + num_count * power}')   

    s = '123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100'
    
    digit_count = 1
    power = 1
    i = 1
    while i < len(s) + 1:
        if i == 10 ** power:
            digit_count += 1
            
        # print(f'i = {i}\tnum = {s[i - 1 : i + digit_count - 1]}')
        
        i += digit_count
    
    return


# counting_series(10)

# print('99')
# # power 2
# print(s[187])
# print(s[188])
# print('100')
# # power 3
# print(s[189])
# print(s[190])
# print(s[191])

# print(s[-3:])
# print(s[-3-2:-3])
# print(s[-3-2-2:-3-2])


"""
Revorse the vewels - page 65
"""


def reverse_vowels(text):
    vowels = 'aeiouAEIOU'
    vowels_in_text = []
    upper_case_position = []
    result = ''
    
    for i in range(len(text)):
        if text[i] in vowels:
            vowels_in_text.append(text[i])
            if text[i].isupper():    
                upper_case_position.append(i)
    
    for i in range(len(text)):
        if text[i] in vowels:
            char_to_add = vowels_in_text.pop(len(vowels_in_text) - 1)
            is_upper = i in upper_case_position
            result += char_to_add.upper() if is_upper else char_to_add.lower()
        else:
            result += text[i]
    
    return result


"""
Everybody on the floor, come do the Scrooge Shuffle - page 66
"""

# not completed
def spread_the_coins(coins, left, right):
    return


"""
Rational lines of action - page 67
"""


def calkin_wilf(n):

    calkin_wilf_queue = collections.deque()
    calkin_wilf_queue.append(fractions.Fraction(1, 1))
    
    
    count = 1
    while count <= n:
        
        fraction = calkin_wilf_queue.popleft()
        
        f1 = fractions.Fraction(fraction.numerator, fraction.numerator + fraction.denominator)
        f2 = fractions.Fraction(fraction.numerator + fraction.denominator, fraction.denominator)
        calkin_wilf_queue.append(f1)
        count += 1
        if count == n:
            return f1
        calkin_wilf_queue.append(f2)
        count += 1
        if count == n:
            return f2
        
    return 'Should not reach here... also, second example test case is WRONG!!!!!!!!! 10000 will yield 43/205, NOT 11/39... to get that, we need n = 1000'


"""
Verbos regulares - page 68
"""

# not completed
def conjugate_regular(verb, subject, tense):
    return


"""
Hippity hoppity, abolish loopity - page 69
"""


def frog_collision_time(frog1, frog2):
    # meet up position = sx + t * dx, sy + t * dy
    # t = (sx1 - sx2) / (dx2 - dx1)
    # t = (sy1 - sy2) / (dy2 - dy1)
    # (sx1 - sx2) * (dy2 - dy1) = (sy1 - sy2) * (dx2 - dx1)
    
    if not can_meet(frog1, frog2):
        return None
        
    pos1 = (frog1[0], frog1[1])
    dir1 = (frog1[2], frog1[3])
    pos2 = (frog2[0], frog2[1])
    dir2 = (frog2[2], frog2[3])
    
    t = 0
    
    try:
        t = (pos1[0] - pos2[0]) // (dir2[0] - dir1[0])
    except: pass

    try:
        t = (pos1[1] - pos2[1]) // (dir2[1] - dir1[1])
    except: pass

    return t if t > 0 else None


def can_meet(frog1, frog2):
    # t = (sx1 - sx2) / (dx2 - dx1)
    # t = (sy1 - sy2) / (dy2 - dy1)
    # (sx1 - sx2) * (dy2 - dy1) = (sy1 - sy2) * (dx2 - dx1)
    return (frog1[0] - frog2[0]) * (frog2[3] - frog1[3]) == (frog1[1] - frog2[1]) * (frog2[2] - frog1[2])


"""
Where no one can hear you bounce - page 70
"""

# not completed
def reach_corner(x, y, n, m, aliens, debug = False):

    corners = [(0, 0), (n - 1, 0), (0, m - 1), (n - 1, m - 1)]
    
    if debug:
        print(f'\ncorners are {corners}')
        print(f'aliens are {aliens}')
        print(f'board dimension is {n} x {m}')
        
        print(f"bishop's position is at {x, y}")
    
    corners_info = [ {
        'point'             : c,
        'alien blocking'    : None 
        } for c in corners ]
    
    aliens_info = [ {
        'point'             : a,
        'blocking corner'   : None
        } for a in aliens  ]
    
    for i in range(len(corners_info)):
        
        vector_to_corner = to_vector_2D( corners_info[i]['point'], (x, y) )
        
        # bishop can only move diagonally
        if is_diagonal_direction(vector_to_corner):
            
            if debug:
                print(f"bishop {x, y} can move to point {corners_info[i]['point']}")
            
            # if no alien when we have valid corner
            if aliens == []:
                if debug:
                    print(corners_info)
                    print('1 return here')
                return True
            
            for j in range(len(aliens_info)):
                
                if aliens_info[j]['blocking corner']:
                    continue
                
                if corners_info[i]['alien blocking']:
                    continue
                
                vector_to_alien = to_vector_2D( aliens_info[j]['point'], (x, y) )
                if is_same_direction(vector_to_corner, vector_to_alien):
                    aliens_info[j]['blocking corner'] = corners_info[i]['point']
                    corners_info[i]['alien blocking'] = aliens_info[j]['point']
                    
                    if debug:
                        print(f"---bishop {x, y} can move to point {corners_info[i]['point']}")

        elif debug:
            print(f"bishop {x, y} cannot move to point {corners_info[i]['point']}")
    
    # check if we have any corner left unblocked
    # if yes, we return True
    for i in range(len(corners_info)):
        
        vector_to_corner = to_vector_2D( corners_info[i]['point'], (x, y) )
        
        if is_diagonal_direction(vector_to_corner) and not corners_info[i]['alien blocking']:
            if debug:
                print(corners_info)
                print('2 return here')
            return True
    if debug:
        print(corners_info)
        print('3 return here')
    return False


# helpers
def to_vector_2D(origin_point, target_point):
    return (target_point[0] - origin_point[0], target_point[1] - origin_point[1])


def to_point_2D(origin_point, target_point):
    return (target_point[0] - origin_point[0], target_point[1] - origin_point[1])


def is_diagonal_direction(vector):
    print('\tx', vector[0])
    print('\ty', vector[1])
    r = abs(vector[0]) == abs(vector[1]) != 0
    print('is diagonal', r)
    return r

def is_same_direction(vector1, vector2):
    cross_product = numpy.cross(vector1, vector2)
    # print(f'cross_product of vector1 {vector1} and vector2 {vector2} is {cross_product}')
    return cross_product == 0


# print(reach_corner( 0, 2, 5, 5, [], debug = True ) )
# print(reach_corner( 4, 4, 9, 9, [(0, 0), (0, 8), (8, 0), (8, 8)], debug = True ) )
# print(reach_corner( 1, 1, 1000, 2, [(0, 0), (0, 1), (999, 0)], debug = True ) )
# print(reach_corner( 1, 1, 1000, 2, [(0, 0), (0, 1), (999, 1)], debug = True ) )
# print(reach_corner( 3, 2, 4, 4, [(1, 2), (0, 1)], debug = True ) )
# print(reach_corner( 3, 2, 5, 4, [(2, 2), (1, 4)], debug = True ) )

# print(reach_corner( 0, 2, 5, 5, [], debug = False ) )
# print(reach_corner( 4, 4, 9, 9, [(0, 0), (0, 8), (8, 0), (8, 8)], debug = False ) )
# print(reach_corner( 1, 1, 1000, 2, [(0, 0), (0, 1), (999, 0)], debug = False ) )
# print(reach_corner( 1, 1, 1000, 2, [(0, 0), (0, 1), (999, 1)], debug = False ) )
# print(reach_corner( 3, 2, 4, 4, [(1, 2), (0, 1)], debug = False ) )
# print(reach_corner( 3, 2, 5, 4, [(2, 2), (1, 4)], debug = False ) )


"""
Nearest polygonal number - page 71
"""

# not completed
def nearest_polygonal_number(n, s):
    
    lo, hi = 1, 1
    polynum = calculate_polynum(s, (lo + hi) // 2)
    
    while polynum < n:
        hi *= 2
        print(f'lo, mid, hi = {lo}, {(lo + hi) // 2}, {hi}')
        polynum = calculate_polynum(s, (lo + hi) // 2)
        print('1', polynum)
        
    hi //= 2
    polynum = calculate_polynum(s, (lo + hi) // 2)
    
    while polynum < n:
        lo *= 2
        print(f'lo, mid, hi = {lo}, {(lo + hi) // 2}, {hi}')
        polynum = calculate_polynum(s, (lo + hi) // 2)
        print('2', polynum)
        
    lo //= 2
    
    while lo < hi:
        i = (lo + hi) // 2
        print(f'lo, mid, hi = {lo}, {(lo + hi) // 2}, {hi}')
        polynum = calculate_polynum(s, i)
        print('3', polynum)
        if polynum == n:
            return polynum
        if polynum > n:
            lo += 1
        else:
            hi -= 1
    
    return polynum


def calculate_polynum(s, i):
    return ( (s - 2) * i * i - (s - 4) * i ) // 2

# print(nearest_polygonal_number(5, 3))
# print(nearest_polygonal_number(27, 4))
# print(nearest_polygonal_number(450, 9))
# print(nearest_polygonal_number(10**10, 42))
# print(nearest_polygonal_number(10**100, 91))


"""
Don’t worry, we will fix it in the post - page 72
"""


def postfix_evaluate(items):
    # print(eval(items))
    ops = []
    nums = []

    for item in items:
        if type(item) == str:
            ops.append(item)
        else:
            nums.append(item)

    e = ''
    for i in range(nums):
        return

    return


# postfix_evaluate([2, 3, '+', 4, '*'])


"""
Fibonacci sum - page 99
"""


def fibonacci_sum(n):
    
    n_copy = n
    result = []
    
    for num in fibonacci_sequence(n)[::-1]:
        
        if n > 0 and n - num >= 0:
            result.append(num)
            n -= num
            
        if n <= 0:
            break
        
    return result if sum(result) == n_copy else []


# return the fibonacci sequence not exceed the threshold
def fibonacci_sequence(threshold):
    
    n_0, n_1 = 0, 1
    fib_seq = [n_0, n_1]
    
    while n_1 <= threshold:
        n_0, n_1 = n_1, n_0 + n_1
        fib_seq.append(n_0)
        
    return fib_seq

    # n_0, n_1 = 0, 1
    # yield n_0
    # yield n_1
    
    # while n_1 <= threshold:
    #     n_0, n_1 = n_1, n_0 + n_1
    #     yield n_0

