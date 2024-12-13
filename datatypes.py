
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

# print(nested[0]) #apple
# print(nested[1]) #["banana", "grapes"]
# print(nested[1][0]) #banana

numbers = [0,1,2,3,4,5,6,7,8,9,10]

nested[1][1] = "pineapple"
# print(nested[1][1]) #pineapple

# ? Slicing
#[start : end : step]

newNested = nested[::2]

newEvens = numbers[2:9:3]
newNested = nested[::-1]
# print(newNested)

#! Add elements into list
#* append
fruits.append("orange")
# print(fruits)

#* extend 
fruits.extend(["kiwi", "guvava"]);
# print(fruits)

#* insert
fruits.insert(2,"banana")
# print(fruits)

#! Remove Elements from List

#* Remove
removed = fruits.remove("kiwi")
# print(fruits)
# print(removed)

#* Pop
# ? it returns removed element
popped = fruits.pop()
# print(fruits)
# print(popped)

fruits.pop(2)
# print(fruits)

#* delete

del fruits[2]
# print(fruits)

#*clear
fruits.clear();
# print(fruits)

#! Finding and Counting Elements
nums = [1,2,3,4,5,5,5,6,7,5,6,7,5]
#* Finding
# print(nums.index(5))

#* Counting
# print(nums.count(5))

#! Sorting and Filtering

#* Sorting
nums.sort()
# print(nums)

#* Reversing
nums.reverse()
# print(nums)

#! Copying List
numsCopied = nums.copy()
numsCopied.append(5)
# print(numsCopied)

#! Common list operations
numsCopied = numsCopied + nums.copy()

num1 = [1,2,3,4,5]
num2 = [6,7,8,9]

# num1 += num2.copy()
# print(num1)

#! Repeated 
num2 = num1 * 5
# print(num2)

#! Membership Test
#* To test a element existance in a list
# print(4 in num1);
# print(7 in num1)

#! Length check
# print(len(num1))

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

#! Destructuring
y = (1,2,3)
a,b,c = y
# print(a)

#! All same methods as list can be applied in tuple except adding ,changing and removing elemnts (it means elements can not be changed)

#! Dictionary
#*{key1:value1,key2:value2,...}
#* Key should not include 
myData = {"name":"Aksh", "age":17, "isMinor":True}
print(myData["isMinor"])

#? dict() constructor
myDict = dict(name="Aksh",age=25)
print(myDict)

#? List of Tuples
tupledList = [("name","Dharmik"),("age","32")]
tupledDict = dict(tupledList)
print(tupledDict)
myName = tupledDict.get("name","Wrong Spelling")
print(myName)

#!Changing Values using keys
myDict["name"] = "Darsh"

#! Adding New Pair using above method
myDict["result"] = 89
print(myDict)

#! Diff b/w pop and popItem
# print(myDict.pop()) #error
print(myDict.popitem()) #last inserted item
#! Clearing Dictionary
myDict.clear()
print(myDict)

myNum1 = {"num1":1}
myNum2 = {"num2":2}
myNum3 = {"num3":3}
myNum4 = {"num4":4}

myNum1.update(myNum2)
mergedSecond = myNum3 | myNum4
print(myNum1)
print(mergedSecond)
#! Range
#? range(start, end, step)
startingNumbers = list(range(1,10))
startingNumbers = tuple(range(1,10))
print(startingNumbers)

#! Sets
#* Its mutable (elements can be changed) and contain unique elements
vegetables = {"tomato", "carrot", "beet"}

#? Empty Set
emptySet = {}

#? Set constructor
fromString = set("akkkkssssh");
print(fromString)

numbers = list(range(0,10))
numSet = set(numbers)
print(numSet)

fromRange = set(range(0,5))
print(fromRange)

numFirst = {1,2,3}
numSecond = {3,4,5}

#? Union ( | )
print(numFirst | numSecond)

#? Intersection ( & )
print(numFirst & numSecond)

#? First Diff ( Left Diff = left - right)
print(numFirst - numSecond)

#? Second Diff ( Right Diff = Right - Left)
print(numSecond - numFirst)

#? Symmetric Diff
print(numFirst ^ numSecond)

#! Set Methods
#? Adding elements 
mySet = {1,2,3}
mySet.add(4)
print(mySet)

#? Update Elements
mySet.update([4,5,6])
# print(mySet)



#? Remove Elements
# mySet.remove(7) #Throws error if element does not exist
# print(mySet)

mySet.discard(7) #Don't throw any error if element does not exist
# print(mySet)

#?Pop Methods
popped = mySet.pop()
print(popped)
popped = mySet.pop()
print(popped)
print(mySet)

#? Clear
mySet.clear()
print(mySet)

#! Set Comparison
mySetOne = {1,2}
mySetTwo = {2,3,4}
mySetThree = {2,1}

#? Subset ( <= ) #Both set can be equal
print(mySetOne <= mySetTwo)
print(mySetOne <= mySetThree)

#? Subset ( < ) #Both set can't be equal
print(mySetOne < mySetTwo)
print(mySetOne < mySetThree)

#? Superset #Both set can't be equal
print (mySetTwo > mySetOne)
print (mySetThree > mySetOne)

#? Superset #Both set can be equal
print (mySetTwo >= mySetOne)
print (mySetThree >= mySetOne)

#? Equality
print(mySetOne == mySetTwo)
print(mySetOne == mySetThree)

#! built in Functions
#? len
print(len(mySetTwo))

#? Member Existance Check
print(2 in mySetTwo)
print(2 not in mySetThree)

#? Finding maximum and minimum from set\
print(max(mySetTwo))
print(min(mySetTwo))

#? Finding sum of set elements
print(sum(mySetTwo))

#! Frozen Sets
#* It makes set immutable
frozenVegetables = frozenset(["tomato", "carrot", "beet"])

#! None
#* Intention value absence
myAge = None


