# Write a program that will reverse a four-digit number.Also, it checks whether the reverse is true.

x = int(input("Enter number: "))

y = int(str(x)[:: -1])

print(y)

if (x==y):
    print(True, "Reverse is same as the number")

else:
    print(False, "Reverse is not same as the number")