# Try It Yourself 4-5: Summing a Million
# Make a list of the numbers from one to one million, use min()
#   and max() to make sure.
# Use sum() to see how quickly Python adds them.
numbers = list(range(1, 1_000_000))

print(f"The lowest number is {min(numbers)}.")
print(f"The highest number is {max(numbers)}.")
print(f"The sum of all the numbers is {sum(numbers)}.")
