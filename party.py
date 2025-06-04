n=int(input())
p=int(input())
time=240
remaining_time=time-p
problems_solved=0
for i in range(1,n+1):
    if(remaining_time>0 and remaining_time>5*i):
        remaining_time=remaining_time-5*i
        problems_solved=problems_solved+1
print(problems_solved)








a="hello world hello world"
count=0
for i in a:
    if(i==" "):
        count=count+1
print(count)





s=input()
count_hyphen=s.count('-')
new_str='-'*count_hyphen+s.replace('-',' ')
print(new_str)