# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not
# A narcissistic number (or Armstrong number) is a number that is the sum of its own digits, each raised to the power of the total number of digits in that number.

x = int(input("Enter a number: "))
a = list(str(x))
print(a)
if x == sum(int(i) ** len(a) for i in str(x)):
    print(f"{x} is an Narcissist number")
else:
    print(f"{x} is not an Narcissist number")
