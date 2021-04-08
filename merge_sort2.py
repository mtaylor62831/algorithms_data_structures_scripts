def merge_sort(list, startIndex = 0, endIndex = None):
    """
    Sorts the list in ascending order.
    Returns a new sorted list.

    Divide: find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in previous step.
    Combine: Merge sorted sublists created in previous step.

    This version doesn't use the [:N] slice operation becuase it runs slower than O(n)
    """
    #if the length of the list is 0 or 1 it's already sorted
    if len(list) <= 1:
        return list
    
    if endIndex == None:
        endIndex = len(list) -1
    
    midpoint = (endIndex - startIndex) // 2
    
    #as long as there are more than 1 items in the sublist, split again
    #REVIEW THIS SECTION - ONCE THE SMALLEST LIST IS SORTED HOW TO WE ADD VALUES TO IT
    if startIndex < midpoint:
        merge_sort(list, startIndex, midpoint)
    if midpoint + 1 < endIndex:
        merge_sort(list, midpoint + 1, endIndex)
    
    #handle the merge
    leftIndex = startIndex
    rightIndex = midpoint + 1
    sortedList = []

    #compare values in the right and left hand side and add to the sortedArray
    while leftIndex <= midpoint and rightIndex <= endIndex:
        if list[leftIndex] < list[rightIndex]:
            sortedList.append(list[leftIndex])
            leftIndex += 1
        else:
            sortedList.append(list[rightIndex])
            rightIndex += 1

    #add in any remaining items from the longer list
    while leftIndex <= midpoint:
        sortedList.append(list[leftIndex])
        leftIndex += 1
    while rightIndex <= endIndex:
        sortedList.append(list[rightIndex])
        rightIndex += 1

    return sortedList
    


def verify_sorted(list):
    """
    Verified that a list is sorted in ascending order. Returns true or false.
    """
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

mylist = [5, 1, 3]
sortlist = merge_sort(mylist)
print(verify_sorted(mylist))
print(verify_sorted(sortlist))