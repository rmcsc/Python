# Try It Yourself 4-10: Slices
#
# Use one of the programs from the chapter and add several lines to the
# end then do the following:
# Print the message "The first three items in the list are:" and use a
# slice to place the first three items
# Print the message "Three items from the middle of the list are:" and
# use a slice to place the middle three items
# Print the message "The last three items in the list are:" and use a
# slice to place the last three items

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

print("\nThe first three items in the list are:")
print(players[:3])

print("\nThree items from the middle of the list are:")
print(players[1:4])

print("\nThe last three items in the list are:")
print(players[-3:])
