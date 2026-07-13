# Variables in Python are dynamically typed, meaning you don't have to declare the type of a variable when you create it. The type is inferred from the value assigned to the variable.

from numpy import average


x=5
print(type(x))

x ="hello World"
print(type(x))
name ="Luka"
age =24
height =1.78
student = True
print(type(name))
print(type(age))
print(type(height))
print(type(student))


# Collections in Python are used to store multiple items in a single variable. The most common collections are lists, tuples, sets, and dictionaries.
numbers = [1, 2, 3, 4, 5]
print(type(numbers))
print(numbers)
print(numbers[0])  # Accessing the first element of the list
print(numbers[-1])  # Accessing the last element of the list
# dictionaries are collections of key-value pairs. Each key is unique, and you can use the key to access the corresponding value.
person = {"name": "Luka", "age": 24, "height": 1.78}
print(person["name"])
tuple_example = (1, 2, 3)
print(type(tuple_example))
set_example = {1, 2, 3}
print(set_example)
#IF statemen
age =20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
#for loop
for i in range(5):
    print(i)
#for each loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    #while loop
count = 0
while count < 5:
    print(count)
    count += 1
    #functions
def greet(name):
    print("Hello, " + name + "!")
greet("Luka")
def square(num):
    return num * num
result = square(4)
print(result)
with open("example.txt", "w") as file:
    file.write("Hello, World!")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


    # task1
students={"luka":24,"maria":22,"john":23}

for each in students:
    print(each,students[each])
avg=0
for each in students:
    avg+=students[each]
avg/=len(students)
print(avg)

maxScore =0
for each in students:
    if students[each]>maxScore:
        maxScore=students[each]
        print(each,maxScore)
with open("students.txt","w") as file:
    for each in students:
        file.write(each+" "+str(students[each])+"\n")
    file.write("Average: "+str(avg)+ " MaxScore: "+str(maxScore)+"\n")


numbers = [12,5,18,2,30,11]
maxNum = max(numbers)
minNum = min(numbers)
avgNum = average(numbers)
print("Max:", maxNum, " Min:", minNum, " Average:", avgNum)
def max(numbers):
    maxNum = numbers[0]
    for num in numbers:
        if num > maxNum:
            maxNum = num
    return maxNum
def min(numbers):
    minNum = numbers[0]
    for num in numbers:
        if num < minNum:
            minNum = num
    return minNum
def average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg
