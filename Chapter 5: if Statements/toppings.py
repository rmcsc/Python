# Filename: toppings.py
# A file to practice the use of not, !=
# ... upon later use, it's for having multiple if statements

# Original use of the file:
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# -----------------------------
# New use:
# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")

# -----------------------------
# New use - using if statements with lists, checking for special items:
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")

# -----------------------------
# # New use: checking that a list is not empty
# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("f\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# -----------------------------
# New use: Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
