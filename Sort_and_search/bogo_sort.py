import random

def get_nums(size):
    '''
    Returns a list of the specified size containing random nums between 0 and 200
    '''
    nums = []
    for i in range(0, size):
        nums.append(random.randint(0,200))
    return nums

def is_sorted(values):
    '''
    Checks if the values passed in are sorted in ascending order
    '''
    for i in range(len(values) - 1 ):
        if values[i] > values[i+1]:
            return False
    return True

def bogo_sort(values):
    '''
    Sorts the list by shuffling the items until they are sorted ascending
    VERY BAD
    '''
    passes = 0
    while not is_sorted(values):
        random.shuffle(values)
        passes += 1
    print("It took " + str(passes) + " passes to sort the list.")
    return values

test = get_nums(6)
print(test)
print(bogo_sort(test))
