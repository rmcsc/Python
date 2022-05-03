# Filename: cars.py
# A simple example of if statements in Python

# List cars contains names of car brands. BMW should be printed in
# uppercase. It will be formatted as such using an if statement. Others
# will be title case.

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
