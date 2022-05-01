# Defining a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# This won't work because tuples are immutable
# |---------------------|
# | dimensions[0] = 250 |
# |---------------------|

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
