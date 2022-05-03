# Try It Yourelf 5-2: More Conditional Tests
# Create more tests and add them to conditional_tests.py. Have at least
# one True and one False of the following: tests for equality and
# inequality with strings; tests using the lower() method; numerical
# tests involving equality and inequality, greater than and less than,
# greater than or equal to, and less than or equal to; tests using the
# and keyword and the or keyword; tests whether an item is in a list;
# and tests whether an item is not in a list.

# I decided not to add these tests to conditional_tests.py; rather, I
# decided to have them here. It's more organized that way, I think.

print("\nTesting for equality with strings:")
fruit = 'banana'
print("Is fruit == 'banana'? I predict True.")
print(fruit == 'banana')
print("Is fuit == 'apple'? I predict False.")
print(fruit == 'apple')

print("\nTesting for inequality with strings:")
vegetable = 'tomato'
print("Is vegetable != 'carrot'? I predict True.")
print(vegetable != 'carrot')
print("Is vegetable != 'tomato'? I predict False.")
print(vegetable != 'tomato')

print("\nTesting using the lower() method:")
name = 'John'
print("Is name.lower() == 'john'? I predict True.")
print(name.lower() == 'john')
print("Is name == 'john'? I predict False.")
print(name == 'john')

print("\nTesting numerical equality:")
number = '21'
print("Is number == '21'? I predict True.")
print(number == '21')
print("Is number == '31'? I predict False.")
print(number == '31')

print("\nTesting numerical inequality:")
another_number = '21'
print("Is another_number != '45'? I predict True.")
print(another_number != '45')
print("Is another_number != '21'? I predict False.")
print(another_number != '21')

print("\nTesting greater than:")
age = '18'
print("Is age > '15'? I predict True.")
print(age > '15')
print("Is age > '21'? I predict False.")
print(age > '21')

print("\nTesting less than:")
length = '45'
print("Is length < '60'? I predict True.")
print(length < '60')
print("Is length < '25'? I predict False.")
print(length < '25')

print("\nTesting greater than or equal to:")
height = '6'
print("Is height >= '5'? I predict True.")
print(height >= '5')
print("Is height >= '7'? I predict False.")
print(height >= '7')

print("\nTesting less than or equal to:")
speed = '88'
print("Is speed <= '90'? I predict True.")
print(speed <= '90')
print("Is speed <= '80'? I predict False.")
print(speed <= '80')

print("\nTesting using the and keyword:")
sweet = True
sour = True
print("If sweet == True and sour = True, then True.")
print(sweet == True and sour == True)
print("If sweet == True and sour == False?, then False.")
print(sweet == True and sour == False)

print("\nTesting using the or keyword:")
wheels = 4
engine = True
print("If wheels == 4 or engine = False, then True.")
print(wheels == 4 or engine == False)
print("If wheels == 3 or engine == False?, then False.")
print(wheels == 3 or engine == False)

print("\nTesting whether an item is in a list:")
vehicles = ['plane', 'train', 'automobile']
print("Is 'plane' in vehicles? I predict True.")
print('plane' in vehicles)
print("Is 'helicopter' in vehicles? I predict False.")
print('helicopter' in vehicles)

print("\nTesting whether an item is not in a list:")
fruits = ['pineapple', 'apple', 'kiwi']
print("Is 'lime' not in fruits? I predict True.")
print('lime not in fruits')
print("Is 'kiwi' not in fruits? I predict False.")
print('kiwi' not in fruits)
