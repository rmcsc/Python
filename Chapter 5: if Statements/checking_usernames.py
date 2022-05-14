# Try It Yourself 5-10: Checking Usernames
# Program simulates how websites ensure everyone has a unique username.
# Make a list of five or more usernammes called current_users. Make a
# list of another five usernames called new_users. Make sure one or two
# names are shared between lists. Loop through new_users to see if each
# username has been used. Print a message if it has. If not, print a
# message saying it's available. Make sure comparisson is case
# insensitive (eg. 'John' and 'JOHN' are the same and shouldn't be
# accepted as two entries). Do this by making a copy of the
# current_users list containing lowercase versions of existing users.

# List of current users
current_users = ['Tony', 'Bruce', 'Thor', 'Steve', 'Clint', 'Peter']

# Copy of list of current   users, in lowercase
current_users_lowercase = [user.lower() for user in current_users]

# List of new users
new_users = ['Bucky', 'Peter', 'Wanda', 'Scott', 'Natasha', 'steve']

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print(f"The username {new_user} is already taken. "
              "Please enter a new username.")
    else:
        print(f"The username {new_user} is available.")
