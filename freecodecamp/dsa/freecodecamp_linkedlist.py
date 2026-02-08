class LinkedList:
    class Node: # this stores the data in the linked list
        def __init__(self, element): # initial values when an object of this class Node is instantiated
            self.element = element
            self.next = None # when a node is first created, it points to nothing

    def __init__(self): # when an object of LinkedList class is created, length is set to 0 and first element is set to None
        self.length = 0 # initial length
        self.head = None # initial first element

    def is_empty(self): # if the linked list is empty, check and return true or false
        return self.length == 0 
    
    def add(self, element):
        node = self.Node(element) # Node object instantiated passing the elements
        if self.is_empty():
            self.head = node # if the list is empty, make this new node the first element
        else:
            current_node = self.head # start at the beginning of the list
            while current_node.next is not None: # loop through until we reach the last node
                current_node = current_node.next
            current_node.next = node # link the last node's 'next' pointer to our new node
        self.length += 1 # increase the list size counter

    def remove(self, element):
        previous_node = None # keeps track of the node right before the one we want to delete
        current_node = self.head # start searching from the beginning of the list
        
        # loop until we find the element or reach the end of the list
        while current_node is not None and current_node.element != element:
            previous_node = current_node # move the previous pointer forward
            current_node = current_node.next # move the current pointer forward
            
        if current_node is None: # if the element was not found in the list
            return        
        elif previous_node is not None: # if the element is in the middle or end
            previous_node.next = current_node.next # bypass the current node to remove it
        else: # if the element to be removed is the first node (head)
            self.head = current_node.next # set the second node as the new head
            
        self.length -= 1 # decrease the list size counter

# Testing the code
my_list = LinkedList()
print(my_list.is_empty()) # checks if list is empty (True)

my_list.add(1) # adds 1 to the list
my_list.add(2) # adds 2 to the list
print(my_list.is_empty()) # checks if list is empty (False)
print(my_list.length) # prints the current length (2)

my_list.remove(1) # removes the element 1
print(my_list.length) # prints the updated length (1)