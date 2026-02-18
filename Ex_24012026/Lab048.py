# age = 90
#
# if age > 100:
#     print("You are old")



#Leap Year Program

# year = int(input("Enter the year: "))
#
# if year % 400==0:
#     print("Leap Year")
# elif year % 100==0:
#     print("Not Leap Year")
# elif year % 4==0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")


#Triangle Classifier
# side1 = int(input("Enter the Side1\n"))
# side2 = int(input("Enter the Side2\n"))
# side3 = int(input("Enter the Side3\n"))
#
# if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
#     print("Not a valid triangle")
# elif side1 == side2 == side3:
#     print("Equilateral Triangle")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

# #Factorial
# num = int(input("Enter the number: "))
#
# fact = 1
# for i in range(1,num+1):
#     fact=num*i
# print(f"Factorial of {num} is:",fact)

#Fibonacci
# num = int(input("Enter the number: "))
# a = 0
# b = 1
# for i in range(0,num):
#     print(a,end=" ")
#     c = a+b
#     a = b
#     b = c

num = int(input("Enter the number: "))

a = 0
b = 1
i = 0

while i < num:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1