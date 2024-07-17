# swap the keys and values of a dictionary and store them in another dictionary

original_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print(original_dict.items())

swapped_dict = {}
for key, value in original_dict.items():
    swapped_dict[value] = key

print(swapped_dict)
