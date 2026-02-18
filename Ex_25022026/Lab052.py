#loop and condition together

for i in range(1,10):
    if i%3 == 0:
        print(i, "if condition passed")
    else:
        print(i, "if condition failed, so else executed")


# Continue Statement
for i in range(1,10):
    if i%2 ==0:
        print(i, "is even number")
        continue
    else:
        print(i, "is odd number")
