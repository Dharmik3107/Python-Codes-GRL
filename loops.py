
#! For

#? Syntax 

#Sequential Data

# for item in sequence:
#     #code

#iteration - means number of time loops run

vehicles = ["Bike", "Aeroplane", "Helicopter", "Cruise", "Yacht"]

for index in range(len(vehicles)):
    if(vehicles[index] == "Helicopter"): vehicles[index] = "Copter"

#! For-else & Break
# For loops complete - Else will run || If loops break manually or automatically then else will not run
# for item in vehicles:
#     if(item == "Cruise"): break
#     print(item)
# else:
#     print("Loop Finished")


#? Statements - Continue
for vahan in  vehicles:
    if(vahan == "Aeroplane"): continue
    print(vahan)    
# for i in range(2,5,2):
#     print(i)  

school = {"3rd":40, "4th":50}


# students = {(1,7,8,10):40, (11,12,13):50, (4,5,6):40}

# for student in students:
#     for number in student:
#         print(number, students[student])

# number = [1,2,3,4,5,6,7,8,9]
marks = [40, 50, 35, 33, 20, 15,40, 50, 5]

# for mark in marks:
#     for num in number:
#         print(num, marks[num-1])
#     break

# for num, mark in zip(number, marks):
#     print(num, mark)  

#!element with index
# for num, mark in zip(range(len(marks)), marks):
#     print(num, mark)  
for index, mark in enumerate(marks):
    print(index, mark)


# for k in school:
#     print(k,school[k])

# print(vehicles)
# name = "Kapadiya"

# for char in name:
#     print(char)


#! While

#!range()




#* Infinite Loops