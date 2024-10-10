# When default value is passed


def sum_of_three_numbers(a, b, c=15):
    return a+b+c

result =sum_of_three_numbers(10, 20)
print(result)