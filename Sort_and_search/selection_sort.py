import random

def get_nums(size):
    '''
    Returns a list of the specified size containing random nums between 0 and 200
    '''
    nums = []
    for i in range(0, size):
        nums.append(random.randint(0,200))
    return nums

def selection_sort(values):
    sorted = []
    while len(values) > 0:
        index_to_move = get_min_index(values)
        sorted.append(values.pop(index_to_move))
    return sorted

def get_min_index(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index   

test = get_nums(14)
print(test)
print(selection_sort(test))
            