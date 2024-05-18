number = (1, 2, 3, 4, 5, 6, 7, 8, 9)                     
num_odd = 0
num_even = 0
for num in number:
   if num%2==0:
       num_even = num_even+1
   else:
       num_odd = num_odd+1
print("the no. of odd numbers are:",num_odd)
print("the no. of even numbers are:",num_even)