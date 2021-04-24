from linked_list import LinkedList

def merge_sort(linked_list):
    '''
    Sorts a linked list in ascending order:
    + Recursively divide linked list into sub lists containing one node
    + Repeatedly merge the sublists to produce sorted lists until only one remains.
    Returns a sorted linked list.
    Runs in O(kn log n) time
    '''
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    '''
    Divide the unsorted list at midpoint into 2 sublists
    '''
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
    else:
        size = linked_list.size()
        midpoint = size//2
        #RUNTIME IMPACT - node at index runs in k time where k is the size of the list up to the midpoint
        #this means we have the same k O(n log n) runtime
        midpoint_node = linked_list.node_at_index(midpoint-1)
        left_half = linked_list
        #create a new Linked list and assign the node after the midpoint to be the head
        right_half = LinkedList()
        right_half.head = midpoint_node.next_node
        #then set next node of the midpoint in left list to None
        midpoint_node.next_node = None
        return left_half, right_half

def merge(left, right):
    '''
    Merges 2 linked lists, sorting by data in the nodes
    Returns a new list with all the values from left and right in ascending order.
    '''

    #Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    #add a dummy head to discard later
    merged.add(0)

    #set current to the head of the merge linked list
    current = merged.head

    #get head nodes from the left and right lists
    left_head = left.head
    right_head = right.head

    #iterate over left and right until we reach the tail node of either list
    while left_head or right_head:
        #If the head node of left is None, we are past the tail
        # so we can add all items from the right side
        if left_head is None:
            current.next_node = right_head
            #call next on right to set loop condition to False
            right_head = right_head.next_node
        #Similarly, if the right list is none
        # we add the items from the left list
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            #Not currently at either tail node
            #Grab data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            #if data on the left is less than the right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                #move left head to next node
                left_head = left_head.next_node
            #if data on the left is greater than the right, set current to right node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        #Move current to next node
            current = current.next_node
    #Discard dummy head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged 

 