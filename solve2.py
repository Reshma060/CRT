pan=input()
dc=pan[5:9]
pan1=pan[0:5]
if(len(pan)==10 and pan[-1].isalpha() and dc.isdigit() and pan1.isalpha()):
    print("yes")
else:
    print("no")