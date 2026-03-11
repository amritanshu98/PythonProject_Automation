# Write a program that will check whether the number is armstrong number or not.

x = int(input("Enter a number: "))

if x< 0:
    print("Enter a positive number")
else:
# for 3 digit number
#     a = x%10
#     b = (x//10)%10
#     c = x//100
#     if x == a**3 + b**3 + c**3:
#         print(f"{x} is an Armstrong number")
#     else:
#         print(f"{x} is not an Armstrong number")

# Using For Loop
#     if x == sum(int(i) ** 3 for i in str(x)):
#         print(f"{x} is an Armstrong number")
#     else:
#         print(f"{x} is not an Armstrong number")

# Using List
    a = list(str(x))
    print(a)
    if x == sum(int(i)**len(a) for i in str(x)):
        print(f"{x} is an Armstrong number")
    else:
        print(f"{x} is not an Armstrong number")




# Using While loop
    # temp = x
    # sum = 0
    # while temp >0:
    #     digit = temp % 10
    #     sum += digit ** 3
    #     temp //= 10
    #
    # if x == sum:
    #     print(x,"is an Armstrong number")
    # else:
    #     print(x, "is not an Armstrong number")