# Try It Yourself 4-11: My Pizzas, Your Pizzas
# Using exercise 4-1 (pizzas.py), make a copy of the list of pizzas and call it friend_pizzas.
# Add a new pizza to the original list
# Add a different pizza to friend_pizzas
# Prove they are separate lists using "My favorite pizzas are:", then use a for loop to print the first list.
# Do the same for the othet list, "My friend's favorite pizzas are:".

pizzas = ['cheese', 'chicken', 'pepperoni', 'veggie']
friend_pizzas = pizzas[:]

pizzas.append('margueritta')
friend_pizzas.append('quattro staggioni')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
