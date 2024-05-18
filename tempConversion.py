temp = input("enter the temprature:")                      
degree = int(temp[:-1])
i_convention = temp[-1]
if i_convention.upper()=="F":
   result = int((degree/5)*9+32)
   o_convention = "farenheit"

elif i_convention.upper()=="C":
     result =int( (degree/9)*5-32)
     o_convention = "celsius"

else:
     print("input proper convention")
     quit()

print("the temperature in ",o_convention ,"is",result , "degrees")