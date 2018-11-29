#!/usr/bin/python3

# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head, 1st node from the list ALWAYS  
    def __init__(self): 
        self.head = None
  
    def sortedInsert(self, new_node): 
          
        # Special case for the empty linked list  
        if self.head is None: 
            print(' head is None, data is', new_node.data, '  next is ', new_node.next)
          # new_node.next = self.head 
            new_node.next = None
            self.head = new_node 
  
        # Special case for head at end, head element should be smallest, b/c it's sorted  
        elif self.head.data >= new_node.data: 
            print(' head.data > new data , data is', new_node.data, '  next is ', new_node.next)
            new_node.next = self.head 
            self.head = new_node 
  
        else : 
  
            # Locate the node before the point of insertion 
            current = self.head 
            while(current.next is not None and current.next.data < new_node.data): 
                print('                        data is', new_node.data, '  next is ', new_node.next)
                current = current.next
              
            new_node.next = current.next
            current.next = new_node 
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to prit the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, '    ') 
            temp = temp.next
  
  
# Driver program 
llist = LinkedList() 
new_node = Node(15) 
llist.sortedInsert(new_node) 
new_node = Node(10) 
llist.sortedInsert(new_node) 
new_node = Node(7) 
llist.sortedInsert(new_node) 
new_node = Node(3) 
llist.sortedInsert(new_node) 
new_node = Node(20) 
llist.sortedInsert(new_node) 
new_node = Node(100) 
llist.sortedInsert(new_node) 
new_node = Node(9) 
llist.sortedInsert(new_node) 
print("Create Linked List")
llist.printList() 
