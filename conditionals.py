
#! if-else 
#? It serves only one condition 

# if condition:
#   action/statement
# else:
#   action/statement

num = 1

if num > 10:
    print("true")
else:
    print("false")


#! if-elif-else 
#? It serves multiple conditions

# if condition:
#   action/statement
# elif condition:
#   action/statement
# ...
# else:
#   action/statement
 

if num > 10:
    print("true")
elif num < 5:
    print("precise")
else:
    print("false")

#! nested if-else / if-elif-else

if num > 10:
    if num < 15:
        print(True)
    else:
        print(False)
else:
    if num < 5 & num > 2:
        print("Precise")
    elif num < 2:
        print("Accurate")
    else:
        print(False)

fruits = ["apple", "banana", "mango"]
fruit = input("Enter Your Fruit Name")

if fruit in fruits:
    print(True)
else:
    fruits.append("apple")