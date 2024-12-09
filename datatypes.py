
#! Complex Numbers
y = 3 + 4j

#! List

#* Empty List
fruits = []

#* Mixed type elements in string
myList = [1, "aksh", True]

#* List with elements type of string
fruits = ["apple", "banana", "Mango"]

#* Nested List
nested = ["apple", ["banana", "grapes"], "watermelon"]

print(nested[0]) #apple
print(nested[1]) #["banana", "grapes"]
print(nested[1][0]) #banana

numbers = [0,1,2,3,4,5,6,7,8,9,10]

nested[1][1] = "pineapple"
print(nested[1][1]) #pineapple

# ? Slicing
#[start : end : step]

newNested = nested[::2]

newEvens = numbers[2:9:3]
newNested = nested[::-1]
print(newNested)

#! Tuple
#* elements can not be changed
fruitsTuple = ("apple", "banana", "Mango")

#! Range
startingNumbers = range(1,10)

#! Dictionary
#*{key1:value1,key2:value2,...}
#* Key should not include 
myData = {"name":"Aksh", "age":17, "isMinor":True}
# print(myData["isMinor"])

#! Sets
#* Its mutable (elements can be changed) and contain unique elements
vegetables = {"tomato", "carrot", "beet"}

#! Frozen Sets
#* It makes set immutable
frozenVegetables = frozenset(["tomato", "carrot", "beet"])

#! None
#* Intention value absence
myAge = None


