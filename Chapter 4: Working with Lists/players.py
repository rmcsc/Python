# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)       # prints out all players
print(players[0:3])  # prints out the first three players
print(players[1:4])  # prints out three, skipping the first
print(players[:4])   # prints out from the first to the fourth
print(players[2:])   # prints out from the third to the last
print(players[-3:])  # prints out the last three players

# We can slice a subset in the for loops, too
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
