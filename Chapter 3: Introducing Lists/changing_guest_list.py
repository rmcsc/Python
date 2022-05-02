# Try It Yourself 3-5: Changing Guest List
# Make a list of people, living or deceased, you'd invite to dinner, then print a personalized invitation to them.
invitees = ['Albert Einstein', 'Tony Stark', 'Ant-Man']
print(invitees)

# Stating who can't come
print(
    f"I originally invited {invitees[0]}, {invitees[1]}, and {invitees[2]} to my dinner, but I heard that {invitees[0]} can't make it! Let me invite somebody else...")

# Stating new invitee
invitees[0] = 'Captain Marvel'
print(f"\nThe new invitee is... *drumroll*... {invitees[0]}!")

# Sending out new invites
print(
    f"\n{invitees[0]}! You're the guest of honor tonight. Please come by my party. Be there or be square!")
print(
    f"\nHey, {invitees[1]}! Come by my house for dinner tonight. {invitees[0]} will be there.")
print(
    f"\nI need some of {invitees[2]}'s magic tricks in my dinner party tonight! {invitees[0]} will be there!")
