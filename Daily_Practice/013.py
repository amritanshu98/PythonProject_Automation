# Check Palindrome Number Write a program to check if the given number is a palindrome number.

x = int(input("Enter Number: "))

y = int(str(x) [::-1 ])

if x==y:
    print("Yes, Palindrome Number")

else:
    print("No, Not a Palindrome Number")
