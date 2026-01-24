#Program that calculate the square and cube of any number

import math
num = float(input("Enter the num\n"))

# square = math.pow(num,2)
# square = num**2
square = pow(num, 2)
print("Square of Entered Number:",square)

# cube = math.pow(num,3)
# cube = num**3
cube = pow(num, 3)
print("Cube of Entered Number:",cube)

