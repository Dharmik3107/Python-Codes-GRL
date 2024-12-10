
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

#! Add elements into list
#* append
fruits.append("orange")
print(fruits)

#* extend 
fruits.extend(["kiwi", "guvava"]);
print(fruits)

#* insert
fruits.insert(2,"banana")
print(fruits)

#! Remove Elements from List

#* Remove
removed = fruits.remove("kiwi")
print(fruits)
print(removed)

#* Pop
# ? it returns removed element
popped = fruits.pop()
print(fruits)
print(popped)

fruits.pop(2)
print(fruits)

#* delete

del fruits[2]
print(fruits)

#*clear
fruits.clear();
print(fruits)

#! Finding and Counting Elements
nums = [1,2,3,4,5,5,5,6,7,5,6,7,5]
#* Finding
print(nums.index(5))

#* Counting
print(nums.count(5))

#! Sorting and Filtering

#* Sorting
nums.sort()
print(nums)

#* Reversing
nums.reverse()
print(nums)

#! Copying List
numsCopied = nums.copy()
numsCopied.append(5)
print(numsCopied)

#! Common list operations
numsCopied = numsCopied + nums.copy()

num1 = [1,2,3,4,5]
num2 = [6,7,8,9]

# num1 += num2.copy()
# print(num1)

#! Repeated 
num2 = num1 * 5
print(num2)

#! Membership Test
#* To test a element existance in a list
print(4 in num1);
print(7 in num1)

#! Length check
print(len(num1))

#! Tuple
#* elements can not be changed
fruitsTuple = ("apple", "banana", "Mango")

#! Empty Tuple
myTuple = ()

#! Single Element Tuple
#* Trailling Comma is important
myTupleS = (5,)

#! Mixed Data type
myTupleM = ("apple", 2, "Mango")

#! Nest Tuple 
#* Nested list in tuple is also allowed
myTupleN = (1, (2,3), 4, [4,5])

#!Implicit Tuple
#* Python will automatically recognize a tuple using commas.
x = 1,2,3

#! All same methods as list can be applied in tuple except adding ,changing and removing elemnts (it means elements can not be changed)

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


