# Try It Yourself 3-6: More Guests
# You have a bigger table now. Add three people to the original list of invitees.
invitees = ['Captain Marvel', 'Tony Stark', 'Ant-Man']
print(invitees)

# Explain you have more space.
print(
    f"I found a larger table, so I now have more space. The original invitees were: {invitees[0]}, {invitees[1]}, and {invitees[2]}.")
print("Adding Thor, Jane Foster, and Darcy Lewis to the table.")

# insert and append three people
invitees.insert(0, "Thor")
invitees.insert(2, "Jane Foster")
invitees.append("Darcy Lewis")

print(invitees)

# Send invites
print(
    f"{invitees[0]}! My man! bring your hammer 'round my house for a dinner party.")
print(f"{invitees[1]}, you're invited to my galactic dinner party tonight.")
print(
    f"{invitees[2]}: a dinner party without you would be more fun, but whatever. Come on by.")
print(f"Hey {invitees[3]}! Come by my dinner party tonight. Bring Jarvis.")
print(
    f"Who better to bring magic than {invitees[4]}? Drop by my house tonight!")
print(
    f"We need a doctor. A good doctor. A fun one. How about you, Dr. {invitees[5]}?")
