# Try It Yourself 5-8: Hello Admin
# Make a list of five or more usernmes, including the name 'admin'.
# Write code that will print a greeting to each user after logging in
# to a website. Loop through the list and print a greeting to each user.
# If usernameis 'admin', print a special greeting. If not, print a
# generic greeting.

usernames = ['admin', 'Spider-Man', 'Dr. Strange',
             'Scarlet Witch', 'Iron Man', 'Star Lord']

for username in usernames:
    if username == 'admin':
        print("Hello, admin! Would you like to view today's reports?")
    else:
        print(f"Hello, {username}! Welcome back to the site.")
