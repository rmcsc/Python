# Try It Yourself 4-13: Buffet
# Store five foods in a tuple
# Use a for loop to print the foods
# Try to modify an item and make sure Python rejects the change
# Replace two items in the tuple, using a for loop to print the items
foods = ('tacos', 'pizza', 'burgers', 'salad', 'ribs')

print("\nThe restaurant offers:")
for food in foods:
    print(food)

print("\nThe restaurant tries to change the tacos for burritos, and the salad for fruit, but fails...")
# foods[0] = 'burritos'
# foods[3] = 'fruit'
for food in foods:
    print(food)

print("\n\tCHANGE REJECTED!")

print("\nThe restaurant changes the menu successfully:")
foods = ('burritos', 'pizza', 'burgers', 'fruit', 'ribs')
for food in foods:
    print(food)
