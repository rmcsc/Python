# Try It Yourself 5-3: Alien Colors #1
# Create a variable called alien_color and assign 'green', 'yellow' or
# 'red'. Write an if statement to test whether the color is green. If it
# is, print a message that the player just earned 5 points. Write
# a version where the if test is passed and another where it isn't.

# Passing test
alien_color = 'green'

if alien_color == 'green':
    print("Player 1 wins 5 points!")

# Failing test
alien_color = 'yellow'

if alien_color == 'green':
    print("Player 1 wins 5 points!")
