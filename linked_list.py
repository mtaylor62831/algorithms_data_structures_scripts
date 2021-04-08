class Node:
    '''
    An object for storing a node in a linked list.
    Models 2 attributes: the data, and a link to the next node in the list.
    '''
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return F"<Node data : {self.data}, next node : self.next_node>"

class LinkedList:
    '''
    Singly linked list.
    '''
    #constuctor instantiates the head property
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        '''
        Returns the number of nodes in the list. Takes linear time.
        '''
        current = self.head
        count = 0
        #you can just write "while current:"
        while current != None:
            count += 1
            current = current.next_node
        return count
    
    def prepend(self, data):
        '''
        Adds a new node containing data at the start of the list.
        This takes O(1) time (constant time).
        '''
        new_head = Node(data)
        new_head.next_node = self.head
        #the new node points to the old head
        #then we set it as the new head of the line
        self.head = new_head
    
    def search(self, value):
        '''
        Searches for the first node with data that matches value. Takes linear time.
        Returns the node if found and None if the value is not in the linked list.
        '''
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next_node
        return None

    def insert(self, data, position = 0):
        '''
        Inserts a new Node containging data at index position
        Insertion takes O(1) but finding the node at the insertion point takes O(n) time
        
        Overall time efficiency is O(n)
        '''
        if position == 0:
            self.prepend(data)
        else:
            new_node = Node(data)
            current = self.head
            count = 1
            #stop 1 short of the insertion position because we need to use next_node to remap
            while count < position - 1:
                count += 1
                current = current.next_node
            #the new node points to the next node in the list
            new_node.next_node = current.next_node
            #the current node is update to point at the new node
            current.next_node = new_node
    
    def remove(self, value):
        '''
        Removes the first occurrance of a Node whose data matches the value.
        Returns the Node or None if the value is not found.
        Runs in O(n) time.
        '''
        current = self.head
        previous = None
        found = False

        while current and not found:
            #special case - value is the first node so we don't need to account for the previous node
            if current.data == value and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == value:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current

    def removeIndex(self, index):
        '''
        Remove the Node at the specified index. Returns the Node that was removed.
        Takes O(n) time since you have to traverse list to the given index.
        '''
        count = 1
        current = self.head
        previous = None

        if index == 1:
            self.head = current.next_node
        
        while current and count < index:
            previous = current
            current = current.next_node
            count += 1
        previous.next_node = current.next_node
        return current
         
    def __repr__(self):
        '''
        Returns a string representation of the list
        Takes O(n) time
        '''
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append(F"[Head: {current.data}]")
            elif current.next_node == None:
                nodes.append(F"[Tail: {current.data}]")
            else:
                nodes.append(F"[{current.data}]")
            current = current.next_node
        #repr functions are required to return a string     
        return " -> ".join(nodes)