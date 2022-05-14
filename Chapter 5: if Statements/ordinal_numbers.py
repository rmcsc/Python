# Try It Yourself 5-11: Ordinal Numbers
# Ordinals indicate a position in a list (eg. 1st, 2nd). Most end in th,
# except 1, 2, and 3. Store numbers 1 through 9 in a list and loop
# through the list. USe if-elif-else chain inside the loop to print the
# proper ordinal ending for each number. Have each result on a separate
# line.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
