first_name = "ada"
last_name = "lovelace"

# for Python 3.6+
full_name = f"{first_name} {last_name}"
# for Python 3.5 or earlier
# full_name = "{} {}".format(first_name, last_name)

message = f"Hello, {full_name.title()}!"
print(message)
