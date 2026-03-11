# Write a program to print all the unique combinations of two digits from 1 to 4 for ex (1,2), (2,3)....

for i in range (1,5):
    for j in range (i+1,5):
        print(f"({i},{j})")


