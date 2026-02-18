# def print_argument(*args):  # ["pramod","amit","lucky"]
#     for i in args:
#         print(i, end="\n")

def print_args(*args):
    for i in args:
        print(i, end=" ")

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