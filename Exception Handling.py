def do_stuff_with_number(n):
        print(n)

the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError: # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)
#this interprets the rest of the numbers in the list as zero's.

#Ending Exercise

actor = {"name": "Isiah Burman", "rank": "awesome"}
#using the split command to print the last name
def get_last_name():
    return actor["name"].split()[1]

get_last_name()
print("All exceptions caught! Good job Programmer!")
print("The actor's last name is %s" % get_last_name())