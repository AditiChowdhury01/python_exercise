
l = []
num = [x for x in input().split(',')]
for i in num:
    x = int(i,2)
    if(i%5==0):
        l.append(i)
print(','.join(l))