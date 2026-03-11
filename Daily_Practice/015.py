# Calculate income tax for the given income by adhering to the below rules first 10k--> 0% second 10 --> 10% remaining-->20%

x = int(input("Enter Salary: "))

if x <= 10000:
    tax=0
elif 10000<x<20000:
    tax = ((x-10000)*0.1)
else:
    tax=((10000*0.1) + (x-20000)*0.2)

print("Tax to be paid is", tax)
