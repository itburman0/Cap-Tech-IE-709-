#Nested Function
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Testing Testing 123"))


def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=8
        print(number)
    printer()
    print(number)

print_msg(9)

def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Destroy us all!")
fun2()

def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5) #5*9 will equal 45
print(multiplywith5(9))