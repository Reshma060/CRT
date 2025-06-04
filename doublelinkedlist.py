class Node:
    def _init_(self,prev,next,data):
        self.prev=None
        self.next=None
        self.data=data
class Doubly_LinkedList:
    def _init_(self):
        self.head=None  
    def insert_beginning(self,data):
        new_node=Node(None,None,data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def delete_beginning(self):
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
ll=Doubly_LinkedList()
ll.insert_beginning(10)
ll.insert_beginning(20)
ll.insert_beginning(30)
ll.insert_beginning(40)
ll.insert_beginning(50)
ll.delete_end()
ll.display()