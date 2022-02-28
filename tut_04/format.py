# Template
my_template = "Hello {0}. Welcome to CPSC {1}!"

# Variables
name = "Akram"
course = 217

# Format the template using the variables
message = my_template.format(name, course)
print(message)

# ALl of the above in 1 line
print("Hello {0}. Welcome to CPSC {1}!".format("Akram", 217))
