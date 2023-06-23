'''
Given two integers return
product if product <= 1000
else return sum

'''

def take_input():
    print("Input two values")
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    return a, b

def product_two_numbers(a, b):
    return a * b

def sum_two_numbers(a, b):
    return a + b


def solution_problem():
    figures = take_input()
    x = product_two_numbers(figures[0], figures[1])
    y = sum_two_numbers(figures[0], figures[1])

    if x <= 1000:
        print("The result is %d " % x)
    else:
        print("The result is %d " % y)

solution_problem()