class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:    
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length-=1
        return temp
    
    ### We can use the same method for Get in DLL but for optimization we are using different
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1,index,-1):
                temp = temp.prev
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length :
            return None
        if index == 0:
            return  self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length +=1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -=1
        return temp
    
          #### Leetcode Interview Questions ####


    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        self.head.value,self.tail.value = self.tail.value,self.head.value

    def reverse(self):
        temp = self.head
        while temp is not None:
            temp.prev,temp.next = temp.next,temp.prev
            temp = temp.prev
        self.head,self.tail = self.tail,self.head

    def is_palindrome(self):
        if self.length <=1:
            return True
        forward_node = self.head
        backward_node = self.tail
        for i in range(self.length // 2):
            if forward_node.value != backward_node.value:
                return False
            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True
    
    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node
            
            self.head = first_node.next
            prev = first_node

        self.head = dummy.next




    

    


    
        
    


    



















my_dooubly_linked_list = DoublyLinkedList(5)
my_dooubly_linked_list.append(7)
my_dooubly_linked_list.append(3)
my_dooubly_linked_list.append(2)
# print(my_dooubly_linked_list.is_palindrome())
# my_dooubly_linked_list.swap_first_last()
# my_dooubly_linked_list.reverse()
# my_dooubly_linked_list.prepend(1)
# print("When Two Nodes")
# print(my_dooubly_linked_list.pop_first())
# print("When one Node")
# print(my_dooubly_linked_list.pop_first())
# print("When no node")
# print(my_dooubly_linked_list.pop_first())
my_dooubly_linked_list.swap_pairs()
my_dooubly_linked_list.print_list()
