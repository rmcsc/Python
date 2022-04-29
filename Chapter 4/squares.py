# Store first 10 square numbers in a list
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

print(f"The lowest (min) nunber is {min(squares)}.\n")
print(f"The highest (max) number is {max(squares)}.\n")
print(f"The sum of all numbers is {sum(squares)}.\n")

# List comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)
