# Try It Yourself 5-9: No Users
# Add an if test to hello_admin.py to make sure the list isn't empty.
# If empty, print "We need to find some users!". Remove usernames from
# list to confirm.

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello, admin! Would you like to view today's reports?")
        else:
            print(f"Hello, {username}! Welcome back to the site.")
else:
    print("We need to find some users!")
