class queue:
    def __init__(self):
        self.q=[]
        self.front=-1
        self.rare=-1
    def enqueue(self,value):
        if(self.front==-1):
            self.front=0
        self.rare+=1
        self.q.append(value)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        value=self.q[self.front]
        self.front+=1
        if self.front>self.rare:
            self.front=self.rare=-1
        return value
    def is_empty(self):
        if rare==-1:
            return self.front==-1 or self.front>self.rare
    def size(self):
        if self.is_empty():
            return 0
        return self.rare-self.front+1
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print(self.q[self.front:self.rare+1])
q=queue()
while True:
    print("\n---Welcome to the Queue methods---")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.To check the queue is_empty or not")
    print("4.Display all the elements")
    print("5.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        value=int(input("Enter the value you want to push:"))
        q.enqueue(value)
    elif choice==2:
        q.dequeue()
    elif choice==3:
        q.is_empty()
    elif choice==4:
        q.display()
    else:
        print("Exit")
        break


