""" String formating """
# python 2 and 3
name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"

message = "Hello %s!" % name # %s is special string
message = "Hello %s %s!" % (name, surname)
print(message)

# in python 3.6
message = f"Hello {name} {surname}. What's up {when}"
print(message)

# multiple string 