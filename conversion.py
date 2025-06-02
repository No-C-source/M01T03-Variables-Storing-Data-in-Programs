#Declare the following variables: 
num1 = 99.23 #convert float into an integer
num2 = 23 #convert integer into a float
num3 = 150 #convert integer into a string
string1 = "100" #convert string into an integer

num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

#Converted as follows: 
print(f"{num1} is a {type(num1)}") #float changed to an integer 
print(f"{num2} is a {type(num2)}") #integer changed to a float
print(f"{num3} is a {type(num3)}") #integer changed to a string
print(f"{string1} is a {type(string1)}") #string changed to an integer