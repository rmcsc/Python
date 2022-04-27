# Try It Yourself 2-7
# Store names in variables with whitespaces (space, \t, \n) in them.
# Print it once with the whitespaces.
# Then print it with the stripping functions: lstrip(), rstrip(), and strip().

name_no_space = "Einstein"
name_left = "   Einstein"
name_right = "Einstein   "
name_left_right = "   Einstein   "
name_tab = "/tEinstein"
name_newline = "Eins\ntein"

print("Variable contents \"as-is\":")   # exiting " so it prints
print(name_no_space)
print(name_left)
print(name_right)
print(name_left_right)
print(name_tab)
print(name_newline)

print("\nVariable contents stripping whitespace left:")
print(name_no_space.lstrip())
print(name_left.lstrip())
print(name_right.lstrip())
print(name_left_right.lstrip())
print(name_tab.lstrip())
print(name_newline.lstrip())

print("\nVariable contents stripping whitespace right:")
print(name_no_space.rstrip())
print(name_left.rstrip())
print(name_right.rstrip())
print(name_left_right.rstrip())
print(name_tab.rstrip())
print(name_newline.rstrip())

print("\nVariable contents stripping all whitespace:")
print(name_no_space.strip())
print(name_left.strip())
print(name_right.strip())
print(name_left_right.strip())
print(name_tab.strip())
print(name_newline.strip())

# Was unsure how to remove \t and \n from strings, so I checked online and found split(), testing:

print("\nVariable contents stripping and splitting all whitespace:")
print(name_no_space.strip().split())
print(name_left.strip().split())
print(name_right.strip().split())
print(name_left_right.strip().split())
print(name_tab.strip().split())
print(name_newline.strip().split())
