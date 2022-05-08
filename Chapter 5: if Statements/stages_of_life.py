# Try It Yourself 5-6: Stages of Life
# Write an if-elif-else chain that determines a person's stage of life.
# Set a value to age, then classify: if less than 2 years old, print
# a message that the person is a baby; at least 2, but less than 4, that
# the person is a toddler; at least 4, but less than 13, that the person
# is a kid; at least 13 but less than 20, a teenager; at least 20 but
# less than 65, an adult; 65 or older, an elder.

age = 13

if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
