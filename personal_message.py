# Try It Yourself 2-3
# Prints a personal message to a user
# (Modified it so the separator isn't a space)

name = "Caribel"
# added sep to eliminate the space that shows up when printing a variable's contents
print("Hello ", name.rstrip(),
      ", would you like to learn some Python today?", sep='')
