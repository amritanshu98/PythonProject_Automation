# Write a program that will give you the sum of digits.

x = int(input("Enter the number: "))

# Method 1 only for 3 digits
if(x>999):
    print("Please enter 3 digit number only")
else:
    a= x%10 #5
    num = x//10 #34
    b = num % 10 #4
    c= num//10 #3
    # c = x//100
    print(a+b+c)

# Method 2 Using While Loop for any number of digits
# def sum_digits(x):
#     sum_digit = 0
#     while x>0:
#         sum_digit = sum_digit + x%10
#         # sum_digit += x%10
#         x = x//10
#     return sum_digit
#
# print(sum_digits(x))


# Method 3 Using Recursion for any number of digits
# def sum_digits(x):
#     if x < 10:
#         return x
#     else:
#         return x%10 + sum_digits(x//10)
#
# print("Sum of Entered Digits:", sum_digits(x))



