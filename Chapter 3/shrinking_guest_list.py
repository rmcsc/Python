# Try It Yourself 3-7
# Womp-womp. The dinner table won't arrive on time, so I only have space for two guests. Let's pop() the guests until two remain.
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

# Woops, table won't arrive in time. Explain you gotta kick some people out.
print("\n\n--------------------\nWOOPS! I only have space for two of you! Gotta clean house.\n")

# Kick out people
kicked_out = invitees.pop()
print(f"Sorry, {kicked_out}. You're out.")
kicked_out = invitees.pop()
print(f"Sorry, {kicked_out}. You're out, too.")
kicked_out = invitees.pop()
print(f"Sorry, {kicked_out}. You too.")
kicked_out = invitees.pop()
print(f"Sorry, {kicked_out}. You didn't bring the fun.")

# Inviting the two people left
print(
    f"\n\nHey, {invitees[0]}. Wanna drop by the party? There's only room for two of you.")
print(f"\nYou too, {invitees[1]}. Wanna come?\n")
