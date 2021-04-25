import random

def get_nums(size):
    '''
    Returns a list of the specified size containing random nums between 0 and 200
    '''
    nums = []
    for i in range(0, size):
        nums.append(random.randint(0,200))
    return nums

def quicksort(values):
    if len(values) <= 1:
        return values
    under_pivot = []
    over_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            under_pivot.append(value)
        else:
            over_pivot.append(value)
    return quicksort(under_pivot) + [pivot] + quicksort(over_pivot)
    
test = get_nums(25)
print(quicksort(test))