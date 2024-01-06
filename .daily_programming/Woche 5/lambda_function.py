# definition:
# the lambda functions are also called "anonymous functions"
# lambda functions can take many arguments, but can only return one expression

# syntax: *lambda arguments: expression* 
# the expression is always executed and returned


# examples using logic:

# using a single argument:

add = lambda a: a + a  # function defined by using keyword "lambda"
print(add(10))  # Output: 20

# using multiple arguments:

add = lambda a, b, c: a + b + c
print(add(10, 10, 10))  # Output: 30

# one difference between a lambda function and a normal function is the difference of the corresponding function types:

# normal function:

def add(a, b, c):
    return a + b + c

result = add(10, 10, 10)
print(result)  # Output: 30

print(type(result))  # Output: <class 'int'>

# lambda function:

add = lambda a, b, c: a + b + c
print(add(10, 10, 10))  # Output: 30

print(type(add))  # Output: <class 'function'>




