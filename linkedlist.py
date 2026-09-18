class node: #creates a node
    def __init__(self, data):#runs when the node is created
        self.data = data#stores the data 
        self.next = None#stores intially there is no next node 
class LinkedList:
    def __init__(self):
        self.head = None#points to the first Node

#traversal
    def traversal(self):
        current = self.head#we will create a variable current which stores the head and move forward
        while current:#runs the loop in list which print the value untill the none 
            print(current)#prints every value 
            current = current.next #jumps to next node untill we reach none 
#insert 
    def insert_in_start(self, data):
        new_node = node(data)#create a new node
        new_node.next = self.head#connect to the head so the new data points to previous head data
        self.head = new_node#inserted data at starting as new head 
#insert at end 
    def insert_in_end(self, data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = new_node


        #deletion 
        # Case 1: the node to delete is the head itself
    def delete_at_start(self, val):
        current = self.head
        if current and current.data == val:
            self.head = current.next
            return
# Case 2: search for the node, keeping track of the one before it
        previous = current
        current = current.next
        while current:
            if current.data == val:
                previous.next = current.next
                return
            previous = current
            current = current.next
        previous = None
        while current and current.data != val:
            current = current.next
            previous = current
        if current is None:
            return
        previous.next = current.next 

            
        
