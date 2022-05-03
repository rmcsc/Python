# Filename: amusement_park.py
# Simple if-elif-else statement

# Checks what age group a person falls in & states their admission cost.
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
# else:
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
