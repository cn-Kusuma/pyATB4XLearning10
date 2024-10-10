# user defined

# 1. Can't return ---No return
# 2 They can return something
# 3 They have parameter
# 4 They don't parameter/arguments

# 1. Can't return ---No return
# No return type and no parameter/Argument
def greet():
    print("Hello")


result = greet()  # NO Return
print(result)


# 2 No return type and with Argument

def greet_by_name(name):
    print("Hello ", name)


greet_by_name("pramod")


# 3 No return type with default argument

def say_hello_default_arg(name="Amit"):
    print("Hello", name)

say_hello_default_arg("pramod")
say_hello_default_arg("")
say_hello_default_arg(name ="Tushar")  # positional argument


#4 Argument+ return type


def sum_of_two_numbers(num1, num2):
    return num1+num2

result = sum_of_two_numbers(10, 34)
print(result)