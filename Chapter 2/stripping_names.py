# Try It Yourself 2-7: Stripping Names
# Store a name in a variable with whitespaces (space, \t, \n) in them.
# Print it once with the whitespaces.
# Then print it with the stripping functions: lstrip(), rstrip(), and strip().

name = "\t Einstein \n"

print("Variable contents \"as-is\":")   # exiting " so it prints
print(name)

print("\nVariable contents stripping whitespace left:")
print(name.lstrip())

print("\nVariable contents stripping whitespace right:")
print(name.rstrip())

print("\nVariable contents stripping all whitespace:")
print(name.strip())
