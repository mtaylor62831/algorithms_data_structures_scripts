def binary_search(list, target):
    start = 0
    end = len(list) - 1
    while start <= end:
        #don't forget about the floor division operator!
        mid = (start + end)//2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        #if the value is not found we call the function again on the portion of the list
        #that COULD contain the result
        elif list[midpoint] < target:
            #the return statement is necessary to make sure that once all calls are evaluated
            #there is something to pass back
            return recursive_binary_search(list[midpoint+1:], target)
        else:
            return recursive_binary_search(list[:midpoint-1], target)

print(recursive_binary_search([1,2,3,4], 6))

def verify(index):
    if index is not None:
        print(F"Target found at index:{index}")
    else:
        print("Target not found.")

test = [2,3,5,6,8,9,11,12,13,17,20]
result = binary_search(test, 5)
verify(result)