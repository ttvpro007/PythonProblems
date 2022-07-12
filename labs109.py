# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":


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
Ascending list
"""


def is_ascending(items):
    if len(items) < 2:
        return True
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False
    return True


"""
Riffle shuffle kerfuffle
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
Even the odds
"""


def only_odd_digits(n):
    return all([int(n) % 2 == 1 for n in str(n)])


"""
Cyclops numbers
"""


def is_cyclops(n):
    if n == 0:
        return True
    without_zero = str(n).split('0')
    return 1 < len(without_zero) < 3 and len(without_zero[0]) == len(without_zero[1])


"""
Domino cycle
"""


def domino_cycle(tiles):
    if len(tiles) == 1:
        return tiles[0][0] == tiles[0][1]
    for i in range(len(tiles)):
        if tiles[i][1] != tiles[(i + 1) % len(tiles)][0]:
            return False
    return True


"""
Colour trio
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
Count dominators
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
Beat the previous
"""


def extract_increasing(digits):
    result = [int(digits[0])]    
    i = 1
    while i < len(digits):
        num = digits[i]
        while int(num) <= result[len(result) - 1] and i < len(digits) - 1:
            i += 1
            num += digits[i]
        if int(num) > result[-1:][0]:
            result.append(int(num))
        i += 1
    return result


"""
Subsequent words
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
Taxi ℤum ℤum
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
Exact change only
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
Rooks on a rampage
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
Try a spatula
"""


def pancake_scramble(text):
    positions = [n for n in range(len(text))]
    for i in range(2, len(text) + 1):
        for index, position in enumerate(positions[:i][::-1]):
            positions[index] = position
    return ''.join([text[positions[i]] for i in range(len(positions))])


"""
Words with given shape
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
Chirality
"""

# not completed
def is_left_handed(pips):
    return


"""
The card that wins the trick
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
Do you reach many, do you reach one?
"""

# not completed
def knight_jump(knight, start, end):
    return


"""
Sevens rule, zeros drool
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
Fulcrum
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
Fail while daring greatly
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
All your fractions are belong to base
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
Count the balls off the brass monkey
"""


def pyramid_blocks(n, m, h):
    # WOLFRAM Sum[(n+i)(m+i), {i, 0, h-1}]
    return h * (1 - 3*h + 2*h*h - 3*m + 3*h*m - 3*n + 3*h*n + 6*m*n) // 6


"""
Count growlers
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
Bulgarian solitaire
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
Scylla or Charybdis?
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
Longest arithmetic progression
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
    n = 0
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
Best one out of three
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
Collecting numbers
"""


def collect_numbers(perm):
    inv_perm = get_inverted_permutation(perm)
    count = 1
    for i in range(len(inv_perm) - 1):
        if inv_perm[i] > inv_perm[i + 1]:
            count += 1
    return count


def get_inverted_permutation(perm):
    inv_perm = [0] * len(perm)
    for i in range(len(perm)):
        inv_perm[perm[i]] = i
    return inv_perm


"""
Between the soft and the NP-hard place
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
Count Troikanoff, I presume
"""


def count_troikas(items):
    element_frequency_dict = get_element_frequency_dict(items)
    #print(element_frequency_dict)
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


def get_element_frequency_dict(items):
    res = {}
    for i in range(len(items)):
        if items[i] not in res:
            res[items[i]] = [i]
        else:
            res[items[i]].append(i)
    return res


"""
Crack the crag
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
Three summers ago
"""


def three_summers(items, goal):
    for i in range(len(items)):
        new_items = get_list_without_element_at_index(items, i)
        if two_summers(new_items, goal - items[i]):
            return True
    return False


def get_list_without_element_at_index(l, i):
    if i not in range(len(l)):
        raise IndexError
    if i == 0:
        return l[ 1 : len(l) ]
    elif i == len(l) - 1:
        return l[ : -1]
    return l[ 0 : i ] + l[ i + 1 : len(l) ]


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
Sum of two squares
"""


import numpy


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
Carry on Pythonista
"""

def count_carries(a, b):
    return


"""
As below, so above
"""


def leibniz(heads, positions):
    return


"""
Expand positive integer intervals
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
Collapse positive integer intervals
"""


def collapse_intervals(items):
    # handles []
    if items == []:
        return ''
    
    sublists = {1:[items[0]]}
    
    # find consecutive sublists
    sublist_count = 1
    for i in range(len(items) - 1):
        if items[i + 1] - items[i] == 1:
            sublists[sublist_count].append(items[i + 1])
        else:
            sublist_count += 1
            sublists[sublist_count] = [items[i + 1]]
            
    return ','.join([str(v[0]) if len(v) == 1 else f'{v[0]}-{v[len(v) - 1]}' for k, v in sublists.items()])


"""
Prominently featured
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
Like a kid in a candy store, except without money
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
Dibs to dubs
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


def get_duplicate_numbers(number):
    
    number_string = str(number)
    start = -1
    number_blocks = []
    
    for i in range(len(number_string) - 1):
        
        if number_string[i] == number_string[i + 1]:
            if start == -1:
                start = i
                
        elif start != -1:
            number_blocks.append(''.join(number_string[start : i + 1]))
            start = -1
            
        # if start != -1 and i == len(number_string) - 2:
        #     number_blocks.append(''.join(number_string[start : i + 2]))        
        
    else:
        if start != -1:
            number_blocks.append(''.join(number_string[start : i + 2]))
            
    return number_blocks


def calculate_score(duplicate_number):
    return 10 ** (len(duplicate_number) - 2)


"""
Nearest smaller element
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
Interesting, intersecting
"""


def squares_intersect(s1, s2):
    return


"""
Fibonacci sum
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

