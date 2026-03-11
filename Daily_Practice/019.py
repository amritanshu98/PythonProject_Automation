# Write a program to print whether a given number is prime number or not

x = int(input("Enter Number: "))
new = []

if x==1:
    print("Not a Prime Number")
else:
#Factors calculation
    for i in range(1,x+1):
        if x%i==0:
           new.append(i)

    if len(new)>2:
        print("Not a Prime Number")
    else:
        print("Prime Number")


    # flag = 0
    # for i in range(2,x):
    #     if x % i == 0:
    #         print("not prime")
    #         flag = 1
    #         break
    # if flag == 0:
    #     print("Prime Number")
