# Sorting items alphabetically in a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

cars.sort()
print("\nHere is the sorted list, changing the order of the original list:")
print(cars)

cars.sort(reverse=True)
print("\nHere is the reverse-sorted list, changing the original:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nBack at it again with the original order (because we overrode the list):")
print(cars)

print("\nHere is the sorted list (temporarily, not changing the variable contents):")
print(sorted(cars))

print("\nHere is the original list again (again, without touching the variable contents):")
print(cars)

print("\nHere we reverse the order of a list using reverse(), permanently:")
cars.reverse()
print(cars)

print("\nBut we can reverse the reversal, like so:")
cars.reverse()
print(cars)

print("\nFind the length of a list using len():", len(cars))
