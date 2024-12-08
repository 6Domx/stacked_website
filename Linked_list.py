class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def remove_beginning(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            if not self.head:  
                self.tail = None
            return removed_data
        else:
            return None
        
    def remove_end(self):
        if not self.head:
            return None
        elif self.head == self.tail: 
            removed_data = self.head.data
            self.head = self.tail = None
            return removed_data
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            removed_data = self.tail.data
            current.next = None
            self.tail = current
            return removed_data
        
    def remove_at(self,data):
        if self.head:
            if self.head.data == data:
                self.remove_beginning()
                return
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    if current.next is None:  
                        self.tail = current
                    return
                current = current.next
    def search(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def print_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
            
