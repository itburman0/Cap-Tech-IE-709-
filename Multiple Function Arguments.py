#the herest" variable is a list of variables, which receives all arguments which were given to the "foo" function after the first 3 arguments. 

def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1,2,3,4,5,6,7,8,9)

#new example
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

#Ending Exercise
#edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1,2,3,4) == 1:
    print("Ehh.")
if foo(1,2,3,4,5) == 2:
    print("Ok.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Warmer.")
if bar(1,2,3,magicnumber = 7) == True:
    print("You are on the Roll Isiah!")