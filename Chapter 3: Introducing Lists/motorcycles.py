# Modifying lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Adds an item to the list without modidfying its prior contents
motorcycles.append('ducati')
print(motorcycles)

# Starts list without contents
motorcycles = []
print(motorcycles)

# Adds items one by one
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Adds an item to a specific position without modifying its prior contents, only their position
motorcycles.insert(0, 'indian')
print(motorcycles)

# Remove specific element from list
# When removed using del, the item is deleted and can't be used later on
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Popping an item from the list
# When you pop an item, you remove the top item from the stack but it's still available to be used in the code
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcyle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)

# Example usage of pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing items by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Using remove() can also allow you to work with the value, but it's just storing it in a variable
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# The remove() method only removes the first occurence of the value
