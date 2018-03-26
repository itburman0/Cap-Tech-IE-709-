# This prints out "Hello, Isiah!"
name = "Isiah"
print("Hello, %s!" % name)

# This prints out "Isiah is 27 years old."
name = "Isiah"
age = 27
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

#notes:
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of
#digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

#Excercise

data = ("Isiah", "Burman", 19.06)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)