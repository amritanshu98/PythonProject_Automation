# Swap the number without using third variable

x= int(input("Enter the value of x: "))
y= int(input("Enter the value of y: "))

x=x+y
y=x-y
x=x-y
print("The value of x after swapping:",x)
print("The value of y after swapping:", y)

#or

# x,y = y,x
# print("x: ", x, "y: ", y)

