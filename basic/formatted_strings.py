# used when we want to dynamically generate some text using some of the variables

first = "Mohit"
last = "Manglani"

message = first + " [" + last + "] is a coder" # non formatted form

msg = f"{first} [{last}] is a coder" # formatted form using the prefix f
# print(message)
print(msg)