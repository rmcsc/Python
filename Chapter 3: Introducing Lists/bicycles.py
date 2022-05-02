# Handling lists, printing from a list, and how indexes work

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())  # first item in the list, capitalized
print(bicycles[1])          # second item in the list
print(bicycles[3])          # fourth item in the list
print(bicycles[-1])         # last item in the list
print(bicycles[-2])         # second to last item in the list

message = f"My first bicycle was a {bicycles[3].title()}."

print(message)
