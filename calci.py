class calculator:
    def _init_(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
object=calculator
print(object.add(10,20))
print(object.sub(10,20))
print(object.mul(20,40))
print(object.div(0,9))

ch=int(input("enter your choice"))
if(ch==1):
    print(object.add(13,89))
elif(ch==2):
    print(object.sub(23,22))
elif(ch==3):
    print(object.mul(8,9))
else:
    print(object.div(1,10))