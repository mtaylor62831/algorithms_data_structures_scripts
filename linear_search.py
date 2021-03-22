def linear_search(list, target):
    """
    Returns the position of the target if found. Otherwise returns None.
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(F"Target found at index:{index}")
    else:
        print("Target not found.")

test = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(test, 5)
verify(result)