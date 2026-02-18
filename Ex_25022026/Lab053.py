#Multiple conditions
#Match Case: similar to switch statement
#Used for multiple if-else loops
# match statement is introduced in python 3.10

num = int(input("Enter a Number: "))
match num:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered ")
    case _: #_ represents default case
        print("No idea")


# name = input("Enter Name: ")
# match name:
#     case "Amit":
#         print("Welcome Amit")
#     case "Sneha":
#         print("Welcome Sneha")
#     case "Priyanka":
#         print("Welcome Priyanka")
#     case _:
#         print("Welcome, is there anybody else?")


browser = str(input("Enter Browser Name: "))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed")
    case "firefox":
        print("Firefox code executed")
    case "safari":
        print("Safari code executed")
    case "edge":
        print("Edge code executed")
    case _:
        print("No Idea")




