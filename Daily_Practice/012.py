# Write a python program to search a given number from a list

my_list = [1,2,3,4,5,6,7,8,9,10]

x = int(input("Enter number:"))

for i in my_list:
    if i == x:
        print("Number Exist")
        break
else:
    print("Number does not exist")

