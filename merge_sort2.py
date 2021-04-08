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
    
    #once we get down to a single item we need to return it in a list
    #unclear to me if this solves the runtime issue
    #tradeoff seems to be creating a bunch of little arrays
    if startIndex == endIndex:
        sublist = []
        sublist.append(list[startIndex])
        return sublist
    
    if endIndex == None:
        endIndex = len(list) -1
    
    midpoint = (endIndex - startIndex) // 2 + startIndex
    
    #as long as there are more than 1 items in the sublist, split again
    if startIndex <= midpoint:
        leftList = merge_sort(list, startIndex, midpoint)
        #once we have a viable list update the start position
        #startIndex += len(leftList)
    if midpoint + 1 <= endIndex:
        rightList = merge_sort(list, midpoint + 1, endIndex)
    
    #Handle the sort and merge for sublists
    sortedList = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(leftList) and rightIndex < len(rightList):
        leftVal = leftList[leftIndex]
        rightVal = rightList[rightIndex]
        if leftVal < rightVal:
            sortedList.append(leftVal)
            leftIndex += 1
        else:
            sortedList.append(rightVal)
            rightIndex += 1
    while leftIndex < len(leftList):
        leftVal = leftList[leftIndex]
        sortedList.append(leftVal)
        leftIndex += 1
    while rightIndex < len(rightList):
        rightVal = rightList[rightIndex]
        sortedList.append(rightVal)
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

mylist = [3, 1, 14, 5, 6, 4]
sortlist = merge_sort(mylist)
print(verify_sorted(mylist))
print(verify_sorted(sortlist))
print(sortlist)