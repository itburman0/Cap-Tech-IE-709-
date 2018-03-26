#Use of Boolean Variables
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

#Boolean Operators
name = "Isiah"
age = 27
if name == "Isiah" and age == 27:
    print("Your name is Isiah, and you are also 27 years old.")

if name == "Isiah" or name == "Rick":
    print("Your name is either Isiah or Rick.")

    name = "Isiah"
if name in ["Isiah", "Rick"]:
    print("Your name is either Isiah or Rick.")

#If Else statements
x = 2
if x == 7:
    print("x equals two!")
else:
    print("x does not equal to two.")
# Not Operator
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

#Exercise
#Changed the number to 16 then took out the 3 in the second array to make the if statements reflect
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")