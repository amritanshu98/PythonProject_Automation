# def print_argument(*args):  # ["amrit","amit","lucky"]
#     for i in args:
#         print(i, end="\n")

def print_args(*args):
    for i in args:
        print(i, end="\n")

print_args(1,2,3)
print_args("Amit", "Prince","Sumit","Lucky")

# *args -> List
# a = ["pramod", "amit", "lucky"]
# for i in a:
#     print(i)
#
#
# for i in range(1, 10):
#     print(i)
# #
# print_argument("pramod", "amit", "lucky")


# Sum any amount of numbers
def sum(*args):
    total=0
    for i in args:
        total +=i
    return total

# Multiply any amount of numbers
def multiply(*args):
    total=1
    for i in args:
        total *=i
    return total


print(sum(1,2,3,4,5))

print(multiply(1, 2, 3, 4, 5))

