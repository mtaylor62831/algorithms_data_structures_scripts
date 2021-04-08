def merge_sort(list):
    """
    Sorts the list in ascending order.
    Returns a new sorted list.

    Divide: find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in previous step.
    Combine: Merge sorted sublists created in previous step.

    Takes O (kn log n) runtime
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists.
    Returns 2 sublists: left and right.
    
    Overall takes O(log n) time. *technically k log n since the slice op does not run in constant time
    """
    midpoint = len(list)//2 
    left = list[:midpoint]
    right = list[midpoint:]
    return left, right

def merge(left, right):
    """
    Merges two lists, sorting them in the process.
    Returns a new merged list
 
    Runs in O(n) time. For a list of size n, there are n merge steps.
    """

    sortedList = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1
    
    #handle situation where right list is shorter than the left
    while i < len(left):
        sortedList.append(left[i])
        i += 1
    
    #handle situation where left list is shorter than right list
    while j < len(right):
        sortedList.append(right[j])
        j += 1
    return sortedList

def verify_sorted(list):
    """
    Verified that a list is sorted in ascending order. Returns true or false.
    """
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

mylist = [22,11,43, 100, 12, 13, 56, 44, 32]
sortlist = merge_sort(mylist)
print(verify_sorted(mylist))
print(verify_sorted(sortlist))