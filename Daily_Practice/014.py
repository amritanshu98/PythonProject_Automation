# Create a new list from a two list using the following condition Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [10,11,12,13,14,15,16,17,18]
new_list = []

for i in l1:
    if i%2 != 0:
        new_list.append(i)
for j in l2:
    if j%2 == 0:
        new_list.append(j)

print(new_list)
