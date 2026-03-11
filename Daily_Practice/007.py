# Write a program that will take three digits from the user and return the square of each digit.

x = int(input("Enter a three digit number: "))

a = x%10
num = x//10
b = num%10
c=num//10

print(c**2,a**2, b**2)