# Try It Yourself 3-8
# Think of 5 places in the world you'd like to visit.
# Store them in a list, making sure it's not in alphabetical order.
places = ['Tokyo', 'San Francisco', 'Rome', 'Argentina', 'Germany']

# Print the list in original order; print it raw, not neat.
print("\nOriginal order:")
print(places)

# Use sorted() to print list alphabetically, without modifying the list.
print("\nAlphabetically using sorted(), without modifying the list:")
print(sorted(places))

# Show the list is in original order by printing it.
print("\nShowing that the original is still in order:")
print(places)

# Use sorted() to print the list in reverse alphabetical order.
print("\nUsing sorted() to print the list in reverse, without changing the original:")
print(sorted(places, reverse=True))

# Show the list is in original order by printing it.
print("\nShowing that the original is still in order:")
print(places)

# Use reverse() to change the order of the list. Print the list to show it's changed.
print("\nUsing reverse() to change the order of the list:")
places.reverse()
print(places)

# Use reverse() to change the order of the list again. Print the list to show it's back to original state.
print("\nUsing reverse() to return the order of the list:")
places.reverse()
print(places)

# Use sort() to change the list to alphabetical order. Print to show the order.
print("\nUsing sort() to sort the list alphabetically:")
places.sort()
print(places)

# Use sort() to change to reverse alphaberical order. Print to show the order.
print("\nUsing sort() to sort the list in reverse alphabetical order:")
places.sort(reverse=True)
print(places)
