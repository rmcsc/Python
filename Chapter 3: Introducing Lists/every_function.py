# Try It Yourself 3-10: Every Function
# Use all functions from this chapter to play around with a list. =)
cities = ['humacao', 'guaynabo', 'isabela',
          'toa baja', 'quebradillas', 'ponce', 'naranjito']

print("\nThe original contents of the list:")
print(cities)

print("\nAccessing index 3 of the list:")
print(cities[3])

print("\nAccessing index 3 of the list, neatly:")
print(cities[3].title())

print("\nAccessing an individual value from the list:")
message = f"My first city was {cities[0].title()}."
print(message)

print("\nChanging the contents of index 3 to San Juan:")
cities[3] = 'san juan'
print(cities)

print("\nAppending elements to the end of the list:")
cities.append('hatillo')
print(cities)

print("\nInserting elements to the list:")
cities.insert(0, 'caguas')
print(cities)
cities.insert(3, 'san sebastián')
print(cities)

print("\nRemoving an item using the del statement:")
del cities[3]
print(cities)

print("\nRemoving using the pop() method:")
popped_city = cities.pop()
print(cities)
print(popped_city)

print("\nUsing pop() in a statement:")
popped_city_in_pr = cities.pop()
print(f"The city of {popped_city_in_pr.title()} is in Puerto Rico.")

print("\nPopping from a position in the list:")
popped_city_where_i_live = cities.pop(2)
print(f"I currently live in {popped_city_where_i_live.title()}.")

print("\nRemoving an item by its value (aka. by name):")
cities.remove('caguas')
print(cities)

print("\nPrinting and using something by name:")
where_i_am_from = 'humacao'
cities.remove(where_i_am_from)
print(cities)
print(f"I am from {where_i_am_from.title()}.")

print("\nSorting alphabetically, permanently, using ___.sort():")
cities.sort()
print(cities)

print("\nChanging the order to reverse alphabetical using ___.sort(reverse=True):")
cities.sort(reverse=True)
print(cities)

print("\nPrinting the list as is:")
print(cities)

print("\nPrinting the sorted list using print(sorted(___)):")
print(sorted(cities))

print("\nPrinting the list as is once again (showing that the previous thing is not permanent):")
print(cities)

print("\nPrinting the list in reverse order using ___.reverse():")
print(cities)
cities.reverse()
print(cities)

print("\nFinding the lenght of the list using len():")
print(len(cities))
