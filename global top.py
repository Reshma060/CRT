global top
def push(value):
    top=-1
    if(top==size-1):   
        return "stack is full"
    else:
        top=top+1
        return stack.append(value)
def pop():
    top=2
    if(top!=-1):
        return stack.pop()
    else:
        top=top-1
        return "stack is empty"
top=-1
size=5
stack=[]
push(20)
push(30)
push(40)
pop()
print(stack)
'''

stack

'''
stack=[]
top=-1
def push(value):
    global top
    stack.append(value)
    top+=1
def pop():
    global top
    if top== -1:
        print("Stack is empty.Nothing to pop.")
        return
    else:
        stack.pop()
        top-=1
def peek():
    if top==-1:
        return "Stack is empty.No top element is there"
    else:
        return f"top element={stack[top]}"
def display():
    if(top==-1):
        print("empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])
push(10)
push(30)
push(50)
push(70)
pop()
pop()
print(peek())
display()
'''
'''
while True:
    print("\n-----Welcome-----")
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.dispaly")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        value=int(input("Enter the element you want to push"))
        push(value)
    elif choice==2:
        pop()
    elif choice==3:
        print(peek())
    elif choice==4:
        dispaly()          
    else:
        print("Exit")
        break
        print("Invalid choice.please try again.")
'''
'''
class queue:
    def __init__(self,value):
        self.Q=[]
        self.value=value
        self.front=-1
        self.rare=-1
    def enqueue(self,Q,value):
        if(self.front==-1):
            self.front=0
        self.rare=self.rare+1
        self.Q.append(value)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        value=self.queue[self.front]
        self.front+=1
        if self.front>self.rare:
            self.front=self.rare=-1
        return value
    def is_empty(self):
        return self.front==-1 
    def size(self):
        if self.is_empty():
            return 0
        return self.front-self.rare-1
    def display(self):
        if self.is_
q=queue()
q.enqueue
