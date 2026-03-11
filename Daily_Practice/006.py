#Write a program that will tell whether the given number is divisible by 3 & 6.

x = int(input("Enter a number: "))

if x%3==0 and x%6==0:
    print("Number is divisible by both 3 and 6")
else:
    print("Number is not divisible by 3 and 6")
