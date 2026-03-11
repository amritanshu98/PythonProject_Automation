# Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

x = int(input("Enter the number: "))

# y = str(x) # in same order

y = str(x)[::-1] # in reverse order

print(" ".join(y))
