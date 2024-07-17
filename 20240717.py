#Python program that prints elements from two lists in the same for loop
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

# Ensure both lists have the same length
for x, y in zip(list1, list2):
    print(x, y)