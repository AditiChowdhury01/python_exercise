
n = input("enter something:")                   
l = 0
m=0
for i in n:
    if i.isdigit():
        l=l+1
    elif i.isalpha():
        m=m+1
    else:
        pass
print("digits",l)
print("letters",m)