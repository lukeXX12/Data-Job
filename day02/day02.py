# # python basic list comprehension
# numbers = [1,2,3,4,5]
# result = []
# for n in numbers:
#     result.append(n*2)
# print(result )
# print( type(result))


# import numpy as np
# print( np.__version__ + " numpy version")
# numbers = np.array([1,2,3,4,5])
# result = numbers *2
# print(result)
# print( type(result))


# Creating numpy arrays
# import numpy as np
# a =np.array([5,8,10,13])
# print (a)
# print (type(a))
# print (a +5)
# print (a*5)
# b =np.array([1,2,5,12])
# print(a+b)          
# # task1
# prices =np.array([100,200,300,400])
# increased_prices = prices * 1.10
# print(increased_prices)
# #statistics
# numbers = np.array([12,2,6,9,23])
# #mean
# print (numbers.mean())
# #Maximum
# print (numbers.max())
# #Minimum
# print (numbers.min())
# #Sum
# Sum = numbers.sum()
# #standard deviation
# print (numbers.std())

# #Task2
# scores =np.array([84,90,75,99,65,81,70])
# #Scores average
# print(scores.mean())
# #Scores maximum
# print(scores.max())
# #scores minimum
# print(scores.min())
# #scores standard deviation
# print(scores.std())

# # ARRAY Slicing
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print(a[:3]) # first 3 elements
# print(a[-2:])# last 2 elements
# print(a[3:6]) # elements from index 3 to 5

# #Filtering arrays
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print (a[a>=18])
#     #FILTERING ARRAY USING BOOLEAN INDEXING

# #Task 3
# temperatures = np.array([22,28,31,18,35,26,30])
# print(temperatures[temperatures > 30])



#Reading CSV Files
# import numpy as np
# data =np.genfromtxt(
#     "day02/employees.csv",
#     delimiter =",",
#     skip_header =1,
#     dtype =str
# )

#print(data)

import numpy as np
salaries =np.array([
    2200,
    2500,
    3000,
    2800,
    3400,
    4200,
    3900,
    1200,
    5400,
    1100,
    3000
])
print("Average salary:", salaries.mean())
print("Maximum salary:", salaries.max())
print("Minimum salary:", salaries.min())
print("Salaries above 3000:",salaries[salaries>3000])
avg=salary = salaries.mean()
print("salaries below average:", salaries[salaries<avg])
print("Total salary:", salaries.sum())

with open("day02/salaries.txt","w") as file:
    file.write("Average salary: "+str(salaries.mean())+"\n")
    file.write("Maximum salary: "+str(salaries.max())+"\n")
    file.write("Minimum salary: "+str(salaries.min())+"\n")
    file.write("Salaries above 3000: "+str(salaries[salaries>3000])+"\n")
    file.write("Salaries below average: "+str(salaries[salaries<avg])+"\n")
    file.write("Total salary: "+str(salaries.sum())+"\n")


#Bonus Task
updated_salaries= salaries * 1.12
print("Updated salaries after 12% increase:", updated_salaries)
print("average of updated salaries:", updated_salaries.mean())
print("salaries above 3500 after increase:",updated_salaries[updated_salaries >3500])