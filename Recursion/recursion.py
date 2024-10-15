# Recursion - a function that calls itself...until it doesn't
# Must have a base case where the function stops calling itself
# Otherwise you'll have what's called a stack overflow

# Not Recursive - Demonstrating Call Stack
# def funcThree():
#     print('Three')

# def funcTwo():
#     funcThree()
#     print('Two')

# def funcOne():
#     funcTwo()
#     print('One')

# funcOne()

# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))