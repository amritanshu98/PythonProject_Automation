#function with multiple arguments

# def allowed(name, password):
#     if name=="Amrit":
#         if password==123:
#             print("You are allowed")
#         else:
#             print("Not allowed")
# allowed("Amrit", 123)
# allowed("Amrit", 1234)


def allowed(name):
    match name:
        case "a":
            print("a is Allowed")
        case "b":
            print("b is Allowed")
        case "c":
            print("c is Allowed")

        case _:
            print("Not Allowed")
allowed("a")
allowed("b")
allowed("c")
allowed("d")



