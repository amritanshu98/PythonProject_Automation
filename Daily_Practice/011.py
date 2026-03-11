# Print all factors of a given number provided by the user.

x = int(input("Enter a number: "))
factors = []

for i in range(1, x+1):
    if x % i == 0:
        factors.append(i)

print("Factors:", factors)
