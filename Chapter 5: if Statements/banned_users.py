# Filename: banned_users.py
# Checking whether a value is not in a list
# Verifying if a user is banned or not based on a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
